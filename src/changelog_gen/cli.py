import click
from changelog_gen.parser import parse_commits
from changelog_gen.generator import generate_changelog
from changelog_gen.utils import get_github_token, create_release

@click.group()
def main():
    """Changelog-Gen CLI"""
    pass

@main.command()
@click.option('--since-tag', required=True, help='Previous git tag to 
start from.')
@click.option('--output', default='CHANGELOG.md', help='Output changelog 
file.')
def generate(since_tag, output):
    """Generate or update CHANGELOG.md"""
    commits = parse_commits(since_tag)
    generate_changelog(commits, output)
    click.echo(f"Changelog updated: {output}")

@main.command()
@click.option('--tag', required=True, help='Git tag for release.')
def release(tag):
    """Create or update GitHub Release"""
    token = get_github_token()
    create_release(tag, token)
    click.echo(f"Release draft updated for tag: {tag}")

if __name__ == '__main__':
    main()

