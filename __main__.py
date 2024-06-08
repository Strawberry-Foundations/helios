from helios.core import Helios
from helios.core.app import app

helios = Helios(app)

if __name__ == "__main__":
    helios.run()
    