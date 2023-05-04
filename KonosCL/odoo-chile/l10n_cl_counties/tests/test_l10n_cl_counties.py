# -*- coding: utf-8 -*-

from odoo.tests.common import TransactionCase, Form


class TestClCounties(TransactionCase):

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.city_08402 = cls.env.ref('l10n_cl_counties.city_cl_08402')
        cls.city_13123 = cls.env.ref('l10n_cl_counties.city_cl_13123')

        cls.partner = cls.env['res.partner'].create({
            'name': 'John Doe',
            'country_id': cls.env.ref('base.cl').id,
        })
        cls.company = cls.env['res.company'].create({
            'name': 'John Inc',
            'country_id': cls.env.ref('base.cl').id,
        })

    def test_full_city_address_for_contacts(self):
        """Check the behaviour of the autocomplete address feature"""
        # Communes with States without parent
        # E.g.: Bulnes -> del Ñuble -> del Ñuble (CL)
        with Form(self.partner) as partner_form:
            partner_form.city_id = self.city_08402
        self.assertEqual(
            self.partner.city, self.city_08402.state_id.name)
        self.assertEqual(
            self.partner.state_id.id, self.city_08402.state_id.id)
        self.assertEqual(
            self.partner.zip, self.city_08402.zipcode)

        # Communes with States with parent
        # Eg.: Providencia -> Santiago -> Metropolitana (CL)
        with Form(self.partner) as partner_form:
            partner_form.city_id = self.city_13123
        self.assertEqual(
            self.partner.city, self.city_13123.state_id.name)
        self.assertEqual(
            self.partner.state_id.id, self.city_13123.state_id.parent_id.id)
        self.assertEqual(
            self.partner.zip, self.city_13123.zipcode)

    def test_full_city_address_for_companies(self):
        """Check that the changes made in the company are reflected on the
        related contact and vice versa"""
        # Changes on the company
        with Form(self.company) as company_form:
            company_form.city_id = self.city_08402
        self.assertTrue(self.company.city)
        self.assertTrue(self.company.state_id)
        self.assertEqual(self.company.city_id, self.company.partner_id.city_id)

        # Changes on the related contact
        with Form(self.company.partner_id) as partner_form:
            partner_form.city_id = self.city_13123
        self.assertTrue(self.company.partner_id.city)
        self.assertTrue(self.company.partner_id.state_id)
        self.assertEqual(self.company.partner_id.city_id, self.company.city_id)
