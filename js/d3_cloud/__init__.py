from fanstatic import Library, Resource
from js.d3 import d3, render_js_d3_new_ie

library = Library('d3_word_cloud', 'resources')

d3_cloud = Resource(library, 'd3.layout.cloud.js',
                    minified='d3.layout.cloud.min.js',
                    depends=(d3,),
                    renderer=render_js_d3_new_ie
                   )
