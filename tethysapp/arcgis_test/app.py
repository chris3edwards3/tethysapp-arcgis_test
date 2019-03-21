from tethys_sdk.base import TethysAppBase, url_map_maker


class ArcgisTest(TethysAppBase):
    """
    Tethys app class for Arcgis Test.
    """

    name = 'ArcGIS Test'
    index = 'arcgis_test:home'
    icon = 'arcgis_test/images/waterfallicon.png'
    package = 'arcgis_test'
    root_url = 'arcgis-test'
    color = '#000000'
    description = 'This is an app developed by Chris Edwards. The purpose was to learn how to use ArcGIS with a tethys app.'
    tags = 'ArcGis'
    enable_feedback = False
    feedback_emails = []

    def url_maps(self):
        """
        Add controllers
        """
        UrlMap = url_map_maker(self.root_url)

        url_maps = (
            UrlMap(
                name='home',
                url='arcgis-test',
                controller='arcgis_test.controllers.home'
            ),
            UrlMap(
                name='watershed',
                url='arcgis-test/watershed.html',
                controller='arcgis_test.controllers.watershed'
            )
        )

        return url_maps
