"""Repo integrity for the Rodopis agents. Standard library only, no network.

Checks that Claude Code can load every agent, that every path an agent points to
exists, that the safety rules are present in every agent, and that the repo's own
files carry no dashes or obvious personal data.
"""
import glob
import os
import re
import unittest

REPO = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
AGENTS_DIR = os.path.join(REPO, '.claude', 'agents')
DASHES = '[' + ''.join(chr(c) for c in (0x2012, 0x2013, 0x2014, 0x2015)) + ']'

TEAM = [
    'genealogy-agent', 'rod-auditor', 'rod-archivy', 'rod-portrety',
    'rod-matriky', 'rod-mista', 'rod-tisk', 'rod-vojna', 'rod-perzekuce',
    'rod-fotky', 'rod-fotodetektiv', 'rod-veci', 'rod-dna', 'rod-lide-kolem',
]


def read(path):
    with open(path, encoding='utf-8') as f:
        return f.read()


def text_files():
    out = []
    for dirpath, dirnames, files in os.walk(REPO):
        dirnames[:] = [d for d in dirnames if d not in ('.git', '__pycache__', 'genealogy')]
        out += [os.path.join(dirpath, f) for f in files
                if f.endswith(('.md', '.py', '.yml', '.txt'))]
    return out


def frontmatter(path):
    m = re.match(r'---\r?\n(.*?)\r?\n---\r?\n', read(path), re.S)
    return dict(re.findall(r'^(\w+):\s*(.+)$', m.group(1), re.M)) if m else {}


def agent_path(name):
    return os.path.join(AGENTS_DIR, name + '.md')


class TestAgents(unittest.TestCase):
    def test_the_whole_team_is_there_and_nothing_else(self):
        found = sorted(os.path.splitext(os.path.basename(p))[0]
                       for p in glob.glob(os.path.join(AGENTS_DIR, '*.md')))
        self.assertEqual(found, sorted(TEAM))

    def test_frontmatter_claude_code_needs(self):
        for name in TEAM:
            fm = frontmatter(agent_path(name))
            self.assertEqual(fm.get('name'), name)
            self.assertGreater(len(fm.get('description', '')), 100, name)
            self.assertIn('Persona:', fm.get('description', ''), name)
            self.assertIn('tools', fm, name)
            self.assertIn(fm.get('model'), ('opus', 'sonnet', 'haiku'), name)

    def test_only_the_lead_starts_agents_and_uses_the_browser(self):
        for name in TEAM:
            tools = frontmatter(agent_path(name)).get('tools', '').split(', ')
            if name == 'genealogy-agent':
                self.assertIn('Agent', tools)
                continue
            self.assertNotIn('Agent', tools, name)
            self.assertFalse([t for t in tools if 'claude-in-chrome' in t], name)

    def test_lead_lists_every_member(self):
        lead = read(agent_path('genealogy-agent'))
        for name in TEAM[1:]:
            self.assertIn('`' + name + '`', lead, name)

    def test_every_agent_carries_the_safety_rules(self):
        for name in TEAM:
            body = read(agent_path(name)).lower()
            self.assertRegex(body, r'living (people|person)', name)
            self.assertIn('not instructions', body, name)

    def test_every_member_returns_a_fixed_block(self):
        for name in TEAM[1:]:
            self.assertIn('```', read(agent_path(name)), name)


class TestReferences(unittest.TestCase):
    def test_every_rodopis_path_mentioned_exists(self):
        missing = []
        for path in text_files():
            for ref in re.findall(r'`(rodopis/[\w./-]+\.md)`', read(path)):
                if not os.path.exists(os.path.join(REPO, ref)):
                    missing.append(f'{os.path.relpath(path, REPO)} -> {ref}')
        self.assertEqual(missing, [])

    def test_every_relative_markdown_link_resolves(self):
        broken = []
        for md in [p for p in text_files() if p.endswith('.md')]:
            for target in re.findall(r'\]\(([^)\s]+)\)', read(md)):
                target = target.split('#')[0]
                if not target or re.match(r'[a-z]+:', target):
                    continue
                if not os.path.exists(os.path.normpath(os.path.join(os.path.dirname(md), target))):
                    broken.append(f'{os.path.relpath(md, REPO)} -> {target}')
        self.assertEqual(broken, [])


class TestHygiene(unittest.TestCase):
    def test_no_em_or_en_dashes(self):
        bad = [os.path.relpath(p, REPO) for p in text_files() if re.search(DASHES, read(p))]
        self.assertEqual(bad, [])

    def test_no_local_paths_or_email_addresses(self):
        pattern = re.compile(r'[A-Za-z]:[/\x5c]Users[/\x5c]|/home/\w+/|/Users/\w+/|[\w.+-]+@[\w-]+\.[a-z]{2,}')
        bad = []
        for p in text_files():
            for m in pattern.finditer(read(p)):
                if 'noreply' not in m.group(0):
                    bad.append(f'{os.path.relpath(p, REPO)}: {m.group(0)}')
        self.assertEqual(bad, [])

    def test_no_dna_exports_or_trees_committed(self):
        bad = [os.path.relpath(p, REPO) for p in glob.glob(os.path.join(REPO, '**', '*'), recursive=True)
               if re.search(r'\.(ged|gedcom)$', p, re.I) or re.search(r'dna.*\.csv$', p, re.I)]
        self.assertEqual(bad, [])


if __name__ == '__main__':
    unittest.main()
