from detectem.plugin import Plugin


class WPSuperCachePlugin(Plugin):
    name = 'wp-super-cache'
    homepage = 'https://wordpress.org/plugins/wp-super-cache/'
    tags = ['wordpress']

    indicators = [
        {'xpath': '//comment()[contains(.,"Cached page generated by WP-Super-Cache on")]'},
    ]