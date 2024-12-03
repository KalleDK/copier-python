import subprocess
from datetime import date

from jinja2 import Environment
from jinja2.ext import Extension


def git_user_name(default: str) -> str:
    return subprocess.getoutput("git config user.name").strip() or default


def git_user_email(default: str) -> str:
    return subprocess.getoutput("git config user.email").strip() or default


def github_user(default: str) -> str:
    return (
        subprocess.getoutput(
            "gh api -H 'Accept: application/vnd.github+json' /user -q .login"
        ).strip()
        or default
    )


class GitExtension(Extension):
    def __init__(self, environment: Environment):
        super().__init__(environment)
        environment.filters["git_user_name"] = git_user_name  # type: ignore
        environment.filters["git_user_email"] = git_user_email  # type: ignore


class CurrentYearExtension(Extension):
    def __init__(self, environment: Environment):
        super().__init__(environment)
        environment.globals["current_year"] = date.today().year  # type: ignore


class GithubExtension(Extension):
    def __init__(self, environment: Environment):
        super().__init__(environment)
        environment.filters["github_user_name"] = github_user  # type: ignore
