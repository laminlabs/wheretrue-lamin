import nox
from laminci import run_notebooks, upload_docs_artifact
from laminci.nox import run, run_pre_commit


@nox.session
def lint(session: nox.Session) -> None:
    run_pre_commit(session)


@nox.session()
def build(session):
    run(session, "uv pip install --system 'lamindb[jupyter,aws,bionty]' wetlab")
    run_notebooks("./docs")
    run(session, "lndocs --strict")
