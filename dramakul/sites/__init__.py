from dramakul.sites.site import Site
from dramakul.sites.dramacool9 import Dramacool9

SITES = {
    Dramacool9.name: {
        **Dramacool9.meta,
        "cls": Dramacool9
    }
}
