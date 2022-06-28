from invoke import task
from invoke.watchers import Responder

# ORIGINAL
#@task
#def answers(c):
#    responder = Responder(
#        pattern=r" Separate source and build directories",
#        response="n\n",
#    )
#    c.run("sphinx-quickstart docs", watchers=[responder])

@task
def answers(c):
    responder1 = Responder(
        pattern=r" Separate source and build directories",
        response="y\n",
    )
    responder2 = Responder(
        pattern=r" Project name",
        response="Test\n",
    )
    responder3 = Responder(
        pattern=r" Author name\(s\)",
        response="Will\n",
    )
    responder4 = Responder(
        pattern=r" Project release",
        response="\n",
    )
    responder5 = Responder(
        pattern=r" Project language",
        response="\n",
    )
    c.run("sphinx-quickstart docs", watchers=[responder1, responder2, responder3, responder4, responder5])