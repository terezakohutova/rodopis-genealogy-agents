"""Print the INDI records of a GEDCOM file that contain a search text.

Usage: python -I rodopis/gedcom_find.py <file.ged> <text>
Standard library only. Reads the file, never writes it.
"""
import sys


def people(path, needle):
    needle = needle.lower()
    found = 0
    record = []

    def flush():
        nonlocal found
        if record and ' INDI' in record[0] and needle in ''.join(record).lower():
            print(''.join(record), end='')
            found += 1

    with open(path, encoding='utf-8-sig', errors='replace') as f:
        for line in f:
            if line.startswith('0 '):
                flush()
                record = []
            record.append(line)
    flush()
    return found


if __name__ == '__main__':
    if len(sys.argv) != 3:
        print(__doc__.strip())
        sys.exit(0 if '--help' in sys.argv or len(sys.argv) == 1 else 2)
    n = people(sys.argv[1], sys.argv[2])
    print(f'{n} matching people', file=sys.stderr)
