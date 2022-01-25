"""Navigate the various projects tangential to the understory."""

from understory import web
from understory.apps import cache, indieauth_client

app = web.application(
    __name__,
    db=True,
    mounts=(
        cache.app,
        indieauth_client.app,
    ),
)


@app.control(r"")
class Index:
    """Full catalog of software projects."""

    def get(self):
        """Return the index."""
        return app.view.index()


@app.control(r"overstory")
class Overstory:
    """."""

    def get(self):
        """."""
        return app.view.overstory()


@app.control(r"canopy")
class Canopy:
    """."""

    def get(self):
        """."""
        return app.view.canopy()


@app.control(r"liana")
class Liana:
    """."""

    def get(self):
        """."""
        return app.view.liana()


@app.control(r"epiphytes")
class Epiphytes:
    """."""

    def get(self):
        """."""
        return app.view.epiphytes()


@app.control(r"understory")
class Understory:
    """."""

    def get(self):
        """."""
        return app.view.understory()


@app.control(r"gaea")
class Gaea:
    """."""

    def get(self):
        """."""
        return app.view.gaea()
