from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.dropdown import DropDown
from kivy.uix.button import Button


Window.size = (300, 500)

navigation_helper = """
Screen:
    NavigationLayout:
        ScreenManager:
            Screen:
                BoxLayout:
                    orientation: 'vertical'
                    MDToolbar:
                        title: "Menu"
                        elevation: 10
                        left_action_items: [['menu', lambda x: nav_drawer.toggle_nav_drawer()]]
                    Widget:
        MDNavigationDrawer:
            id: nav_drawer
            BoxLayout:
                orientation: 'vertical'
                spacing:'8dp'
                padding:'8dp'
                
                Image:
                    source:'vison.jpg'
                
                MDLabel:
                    text:'              Image Operation'
                    font_style:'Subtitle1'
                    size_hint_y:None
                    height:self.texture_size[1]
                
                
                ScrollView:
                    MDList:
                        OneLineIconListItem:
                            text:'Erosion'
                            IconLeftWidget:
                                icon:'airballoon'

                        OneLineIconListItem:   
                            text:'Dilation'    
                            IconLeftWidget:   
                                icon:'bulma'
                        OneLineIconListItem: 
                            text:'Edge Detection'
                            IconLeftWidget:   
                                icon:'panda'

                        OneLineIconListItem:     
                            text:'Contrast Adjustment' 
                            IconLeftWidget:           
                                icon:'beach' 
                                
                        OneLineIconListItem:     
                            text:'Image Enchance Color' 
                            IconLeftWidget:           
                                icon:'bee-flower' 

                
                                    
                                    
"""




class DemoApp(MDApp):
    def build(self):
        MDApp.title = 'Vision Fixel'
        MDApp.icon = 'eye.png'
        screen = Builder.load_string(navigation_helper)

        return screen


DemoApp().run()