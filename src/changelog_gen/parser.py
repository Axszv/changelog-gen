import subprocess
import re
from collections import defaultdict

CONVENTIONAL_PATTERNS = {
    'feat': re.compile(r'^feat(?:\\(.+\\))?:'),
    'fix': re.compile(r'^fix(?:\\(.+\\))?:'),
    'docs': re.compile(r'^docs(?:\\(.+\\))?:'),
    'chore': re.compile(r'^chore(?:\\(.+\\))?:'),
}

def parse_commits(since_tag):
    """Return a dict grouping commit messages by type since the given 
tag."""
    cmd = ['git', 'log', f'{since_tag}..HEAD', '--pretty=format:%s']
    result = subprocess.run(cmd, capture_output=True, text=True, 
check=True)
    commits = result.stdout.splitlines()

    grouped = defaultdict(list)
    for msg in commits:
        for typ, pattern in CONVENTIONAL_PATTERNS.items():
            if pattern.match(msg):
                grouped[typ].append(msg)
                break
        else:
            grouped['other'].append(msg)
    return grouped

