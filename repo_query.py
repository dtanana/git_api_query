#!/usr/bin/env python3
import click
import http_requests


#Using Click library to make args and options easy readible and documented
@click.command()
@click.option('--releases', help='function to grab the last 2 releases', is_flag=True, default=False)
@click.option('--pull_requests', help='function to grab the last 3 Pull Requests' ,is_flag=True, default=False)
@click.option('--token', help='Making request to a private repo, we got you', default='')
@click.argument('git_url', required=1, type=str)


def repo_query(git_url, releases, pull_requests, token):
    """ repo_query: releases, pull requests, required git_url [github.com/user/repo]"""
    user , repo = http_requests.parse_git_url(git_url)[0], http_requests.parse_git_url(git_url)[1]
    if releases:
        results = http_requests.releases_request(user,repo,token)
        if results is None:
            click.echo("No Releases in this repo.")
            return
        elif results[2] == 4:
            click.echo(results[0] + results[1] + 'Check your command and URL')
            return
        elif results[2] == 5:
            click.echo(results[0] + results[1] + 'Check status.github.com')
            return
        elif results[0][2]:
            click.echo('The three most recent Releasest most recent to least')
            for i in results:
                click.echo(f'Name {i[0]} and the version number(tag) {i[1]}\r')
        click.echo('End of list')

    elif pull_requests:  
        results = http_requests.pulls_request(user,repo, token)
        if results is None:
            click.echo("No Releases in this repo.")
            return
        elif results[2] == 4:
            click.echo(results[0] + results[1] + 'Check your command and URL')
            return
        elif results[2] == 5:
            click.echo(results[0] + results[1]+ 'Check status.github.com')
            return
        elif results[0][2]:
            click.echo('The three most recent Pull Request most recent to least')
            for i in results:
                click.echo(f'Title {i[0]} and the Number {i[1]}\r')
        click.echo('End of list')

    else:
        get_help()

if __name__ == '__main__':
    repo_query()