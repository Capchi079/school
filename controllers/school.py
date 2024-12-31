from odoo import http

class School(http.Controller):
    @http.route('/my/school/', auth='public' ,website=True )
    def screen(self,**kwargs):
        # return 'hello Users'
        val=http.request.env['student.master'].search([])
        return http.request.render('SchoolMaster.meee',{'val':val})
# from odoo import http

class WebsiteContactUs(http.Controller):

    @http.route('/my/contact_us2/', auth='public' ,website=True)
    def contact_us_page(self):

        # return http.request.render('website_contact_us.contact_us_template')
        return http.request.render('SchoolMaster.contact_us_template')
