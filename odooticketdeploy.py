import insert_record_into_database

""" Steps required To Run The Model To insert tickets into odoo help desk database:
1) Run devolper mode in odoo Settings(listed in the end) Then GoTo Setting>Technical>sequence 

2) create a new sequence with sequence code: 'mail.message', Name: CommentID, Prefix:CID , 
sequence size: 5 Step:1, Next Number: 1, Implementation: standard, Active: On and save it

3) Create New Contact For your Employees in CONTACTS if not created make sure that you Add the same exact name as in your External Api Furthermore,
mark: individual option, Add Email of your Employee, Phone or Mobile(Optional) and save it

4) Create a contact in CONTACTS named: Syncro System and save it.

5) add piece of code in the content (after line:180) of mail_message in odoo/addons/odoo_website_helpdesk/models/mail_message
-------------------------------------------------------------------------------------------------------
    comment_id = fields.Char(string='Comment_id', default=lambda self: self._generate_comment_id(),
                             help='The name of the help ticket. By default, a new '
                                  'unique sequence number is assigned to each '
                                  'mail message, unless a name is provided.',
                             readonly=True)

    def _generate_comment_id(self):
        return self.env['ir.sequence'].next_by_code('mail.message') or _('New')

    def create(self, vals):
        if vals.get('comment_id', _('New')) == _('New'):
            vals['comment_id'] = self._generate_comment_id()
        return super('mail.message', self).create(vals)
------------------------------------------------------------------------------------------------------
6) We need to edit the config parameters to apply the changes of step 5
root@TestOdoo2: cd /etc/init.d
root@TestOdoo2:/etc/init.d# nano odoo-server
Goto Line shown below and add -u mail in it
DAEMON_OPTS="-c $CONFIGFILE -u mail"
root@TestOdoo2:/etc/init.d# systemctl daemon-reload
root@TestOdoo2:/etc/init.d# service odoo-server restart
                  OR
6) If using pycharm click three dots(More Actions) at top taskbar, Click Edit
go to the second bar of script and add -u mail in the end and Rerun the compiler.
-------------------------------------------------------------------------------------------------------
7) Edit the configurations in the insert_record_into_database.py according to your settings
-------------------------------------------------------------------------------------------------------
url = 'http://localhost:8069' # Replace with your actual URL
db = 'odoo16'  # Replace with your actual database name
username = 'admin'  # Replace with your actual username
password = 'admin'  # Replace with the user's password
-------------------------------------------------------------------------------------------------------
8) In The odooticketdeploy.py File Add customer_id = '123456789' # Replace customer id with actual id
------------------------------------------------------------------------------------------------------- """

customer_id = '26415261'
insert_record_into_database.insert_customer_by_customer_id(customer_id)
insert_record_into_database.insert_tickets_by_customer_id(customer_id)
insert_record_into_database.insert_all_customer_comments(customer_id)
insert_record_into_database.post_all_customer_comments(customer_id)
insert_record_into_database.update_tickets_by_customer_id(customer_id)
insert_record_into_database.update_all_tickets_in_api(customer_id)