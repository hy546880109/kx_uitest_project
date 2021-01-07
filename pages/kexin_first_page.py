from page_objects import PageElement, PageObject  #引入库

class Kexin_First_Page(PageObject):
    '''首页'''
    first_page_Sidebar = PageElement(css='div.header-con.ivu-layout-header > div > a > i')
    first_page_guanyu = PageElement(css=' div.custom-content-con > div.about')
    first_page_yuyan = PageElement(css='div.ivu-dropdown-rel > a > img')
    first_page_dengchu = PageElement(css='div:nth-child(1) > div > a > i')
    first_page_GIS = PageElement(css='div:nth-child(2) > div > a > i')
    first_page_devices= PageElement(css='div:nth-child(3) > div > a > i')
    first_page_alarm = PageElement(css='div:nth-child(4) > div > a > i')
    first_page_gongdan = PageElement(css='div:nth-child(5) > div > a > i')
