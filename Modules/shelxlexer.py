#!/usr/bin/env python
# -*- coding: utf-8 -*-
# GUI generated with help of wxGlade 0.6.3 on Thu Jan 14 23:40:49 2010
# Author is grateful to people who constantly help in developing of the LinXTL:
# Michel Simard; Theirry Moris; Hein Schaper; Government of Canada and University of Montreal for financial support 
# of my Ph.D theses.
# License: GPL
#GNU GENERAL PUBLIC LICENSE
#Version 3, 29 June 2007
#Copyright (C) Denis Spasyuk
#Everyone is permitted to copy and distribute verbatim copies of this license document, but changing it is not allowed.
#Preamble
#The GNU General Public License is a free, copyleft license for software and other kinds of works.
#The licenses for most software and other practical works are designed to take away your freedom to share and change the works. By contrast, the GNU General Public License is intended to guarantee your freedom to share and change all versions of a program--to make sure it remains free software for all its users. We, the Free Software Foundation, use the GNU General Public License for most of our software; it applies also to any other work released this way by its authors. You can apply it to your programs, too.
#When we speak of free software, we are referring to freedom, not price. Our General Public Licenses are designed to make sure that you have the freedom to distribute copies of free software (and charge for them if you wish), that you receive source code or can get it if you want it, that you can change the software or use pieces of it in new free programs, and that you know you can do these things.
#To protect your rights, we need to prevent others from denying you these rights or asking you to surrender the rights. Therefore, you have certain responsibilities if you distribute copies of the software, or if you modify it: responsibilities to respect the freedom of others.
#For example, if you distribute copies of such a program, whether gratis or for a fee, you must pass on to the recipients the same freedoms that you received. You must make sure that they, too, receive or can get the source code. And you must show them these terms so they know their rights.
#Developers that use the GNU GPL protect your rights with two steps: (1) assert copyright on the software, and (2) offer you this License giving you legal permission to copy, distribute and/or modify it.
#For the developers' and authors' protection, the GPL clearly explains that there is no warranty for this free software. For both users' and authors' sake, the GPL requires that modified versions be marked as changed, so that their problems will not be attributed erroneously to authors of previous versions.
#Some devices are designed to deny users access to install or run modified versions of the software inside them, although the manufacturer can do so. This is fundamentally incompatible with the aim of protecting users' freedom to change the software. The systematic pattern of such abuse occurs in the area of products for individuals to use, which is precisely where it is most unacceptable. Therefore, we have designed this version of the GPL to prohibit the practice for those products. If such problems arise substantially in other domains, we stand ready to extend this provision to those domains in future versions of the GPL, as needed to protect the freedom of users.
#Finally, every program is threatened constantly by software patents. States should not allow patents to restrict development and use of software on general-purpose computers, but in those that do, we wish to avoid the special danger that patents applied to a free program could make it effectively proprietary. To prevent this, the GPL assures that patents cannot be used to render the program non-free.
from __future__ import print_function
import wx
class lexer_class(object):
    def __init__(self, text, fsg, main_font):
            self.text=text
            self.fsg=fsg
            self.main_font=main_font  
            self.shellexer()
    def shellexer(self):
        self.text.SetLexer(wx.stc.STC_LEX_LUA)

        keywords_main =["PART", "CELL", "FLAT", "ZERR", "LIST", "SWAT", "LATT", "SYMM", "L.S.", "FREE", "MPLA", "MORE",
                    "ACTA", "FMAP", "PLAN", "MOVE", "END", "BASF", "HTAB", "CGLS", "BUMP", 'BIND', 
                    "EQIV", "BOND", "WPDB", "CONF", "SIZE",  "TEMP", "WGHT", "FVAR", "MOLE","DAMP", "RESI", "DISP", "ABIN"]
        keywords_main2=["TITL","SFAC",  "11.000000", "11.00000", "UNIT", "AFIX","ANIS", "WGHT", "EXTI", "TWIN", "SADI", "DELU","HFIX","EADP", "TWIN", "FLAT", "RIGU", "SIMU", "HKLF", "SUMP", "DFIX", "OMIT", "DANG", "ISOR", "BLOC", "SHEL"]
        keywords_main3=['data_global','_publ_contact_author_name','_publ_contact_author_address',
                '_publ_contact_author_phone','_publ_contact_author_fax','_publ_contact_author_email',
                '_journal_date_recd_electronic','_journal_date_to_coeditor','_journal_date_from_coeditor',
                '_journal_date_accepted','_journal_date_printers_first','_journal_date_printers_final',
                '_journal_date_proofs_out','_journal_date_proofs_in','_journal_coeditor_name',
                '_journal_coeditor_code','_journal_coeditor_notes','_journal_techeditor_code',
                '_journal_techeditor_notes','_journal_coden_ASTM','_journal_name_full','_journal_year',
                '_journal_volume','_journal_issue','_journal_page_first','_journal_page_last', '_exptl_absorpt_special_details',
                '_journal_suppl_publ_number','_journal_suppl_publ_pages','_publ_section_title',
                '_publ_author_name','_publ_author_address','_publ_section_abstract','_publ_section_comment',
                '_publ_section_exptl_prep','_publ_section_exptl_refinement','_publ_section_figure_captions',
                '_publ_section_table_legends','_publ_section_references','_audit_creation_method', "_space_group_symop_operation_xyz",
                "_shelx_estimated_absorpt_T_min", "_shelx_estimated_absorpt_T_max ", "_diffrn_source", "_diffrn_reflns_av_unetI","netI",
                "_diffrn_reflns_Laue_measured_fraction_max", "_diffrn_reflns_Laue_measured_fraction_full", "_diffrn_reflns_point_group_measured_fraction_max",
                "_diffrn_reflns_point_group_measured_fraction_full", "_reflns_Friedel_coverage","_reflns_Friedel_fraction_max","_reflns_Friedel_fraction_full",
                "_atom_site_site_symmetry_order", "_shelx_res_checksum", "_shelx_hkl_file", "_shelx_hkl_checksum", "_shelx_res_file",
                '_chemical_name_systematic', '_space_group_crystal_system','_space_group_IT_number', "_shelx_SHELXL_version_number",   
                '_space_group_name_H','M_alt', '_space_group_name_Hall',
                '_chemical_name_common','_chemical_melting_point','_chemical_formula_moiety',
                '_chemical_formula_sum','_chemical_formula_weight','_atom_type_symbol',
                '_atom_type_description','_atom_type_scat_dispersion_real', '_refine_ls_abs_structure_Flack',
                '_atom_type_scat_dispersion_imag','_atom_type_scat_source','_symmetry_cell_setting'
                ,'_symmetry_space_group_name_H-M','_symmetry_space_group_name_Hall',
                '_symmetry_equiv_pos_as_xyz','_cell_length_a','_cell_length_b','_cell_length_c',
                '_cell_angle_alpha','_cell_angle_beta','_cell_angle_gamma','_cell_volume',
                '_cell_formula_units_Z','_cell_measurement_temperature','_cell_measurement_reflns_used',
                '_cell_measurement_theta_min','_cell_measurement_theta_max','_exptl_crystal_description',
                '_exptl_crystal_colour','_exptl_crystal_size_max','_exptl_crystal_size_mid',
                '_exptl_crystal_size_min','_exptl_crystal_density_meas','_exptl_crystal_density_diffrn',
                '_exptl_crystal_density_method','_exptl_crystal_F_000','_exptl_absorpt_coefficient_mu',
                '_exptl_absorpt_correction_type','_exptl_absorpt_correction_T_min',
                '_exptl_absorpt_correction_T_max','_exptl_absorpt_process_details','_exptl_special_details',
                '_diffrn_ambient_temperature','_diffrn_radiation_wavelength','_diffrn_radiation_type',
                '_diffrn_radiation_source','_diffrn_radiation_monochromator','_diffrn_measurement_device_type',
                '_diffrn_measurement_method','_diffrn_detector_area_resol_mean','_diffrn_reflns_number',
                '_diffrn_reflns_av_R_equivalents','_diffrn_reflns_av_sigmaI','netI','_diffrn_reflns_limit_h_min',
                '_diffrn_reflns_limit_h_max','_diffrn_reflns_limit_k_min','_diffrn_reflns_limit_k_max',
                '_diffrn_reflns_limit_l_min','_diffrn_reflns_limit_l_max',
                '_reflns_number_total','_reflns_number_gt',  "_exptl_transmission_factor_min", "_exptl_transmission_factor_max",
                '_reflns_threshold_expression','_computing_data_collection','_computing_cell_refinement',
                '_computing_data_reduction','_computing_structure_solution','_computing_structure_refinement',
                '_computing_molecular_graphics','_computing_publication_material','_refine_special_details',
                '_refine_ls_structure_factor_coef','_refine_ls_matrix_type','_refine_ls_weighting_scheme',
                '_refine_ls_weighting_details','_atom_sites_solution_primary','_atom_sites_solution_secondary',
                '_atom_sites_solution_hydrogens','_refine_ls_hydrogen_treatment','_refine_ls_extinction_method',
                '_refine_ls_extinction_coef','_refine_ls_number_reflns','_refine_ls_number_parameters',
                '_refine_ls_number_restraints','_refine_ls_R_factor_all','_refine_ls_R_factor_gt',
                '_refine_ls_wR_factor_ref','_refine_ls_wR_factor_gt','_refine_ls_goodness_of_fit_ref',
                '_refine_ls_restrained_S_all','_refine_ls_shift','su_max','_refine_ls_shift','su_mean',
                '_atom_site_label','_atom_site_type_symbol','_atom_site_fract_x','_atom_site_fract_y',
                '_atom_site_fract_z','_atom_site_U_iso_or_equiv','_atom_site_adp_type','_atom_site_occupancy',
                '_atom_site_symmetry_multiplicity','_atom_site_calc_flag','_atom_site_refinement_flags',
                '_atom_site_disorder_assembly','_atom_site_disorder_group','_atom_site_aniso_label',
                '_atom_site_aniso_U_11','_atom_site_aniso_U_22','_atom_site_aniso_U_33','_atom_site_aniso_U_23',
                '_atom_site_aniso_U_13','_atom_site_aniso_U_12','_geom_special_details',
                '_geom_bond_atom_site_label_1','_geom_bond_atom_site_label_2','_geom_bond_distance',
                '_geom_bond_site_symmetry_2','_geom_bond_publ_flag','_geom_angle_atom_site_label_1',
                '_geom_angle_atom_site_label_2','_geom_angle_atom_site_label_3','_geom_angle',
                '_geom_angle_site_symmetry_1','_geom_angle_site_symmetry_3','_geom_angle_publ_flag',
                '_geom_torsion_atom_site_label_1','_geom_torsion_atom_site_label_2',
                '_geom_torsion_atom_site_label_3','_geom_torsion_atom_site_label_4','_geom_torsion',
                '_geom_torsion_site_symmetry_1','_geom_torsion_site_symmetry_2','_geom_torsion_site_symmetry_3',
                '_geom_torsion_site_symmetry_4','_geom_torsion_publ_flag',
                '_platon_squeeze_void_nr','_platon_squeeze_void_average_x','_platon_squeeze_void_average_y',
                '_platon_squeeze_void_average_z','_platon_squeeze_void_volume',
                '_platon_squeeze_void_count_electrons','_platon_squeeze_void_content','_platon_squeeze_details',
                '_refine_diff_density_min','_refine_diff_density_rms',  '_geom_hbond_atom_site_label_D','_geom__atom_site_label_H', '_geom_hbond_atom_site_label_A',
                '_geom_hbond_distance_DH', '_geom_hbond_distance_HA', '_geom_hbond_distance_DA',  '_geom_hbond_angle_DHA', '_geom_hbond_site_symmetry_A', '_refine_diff_density_max', '_shelxl_version_number',
                '_chemical_absolute_configuration', '_refine_ls_extinction_expression', '_refine_ls_abs_structure_details', '_space_group_name_H-M_alt', '_reflns_special_details', 
                '_atom_site_refinement_flags_posn', '_atom_site_refinement_flags_adp', '_atom_site_refinement_flags_occupancy']
        keywords_main4=["loop_", "_diffrn_measured_fraction_theta_max", "_diffrn_measured_fraction_theta_full", "_diffrn_reflns_theta_min", "_diffrn_reflns_theta_full", "_diffrn_reflns_theta_max"]
      
        self.text.SetKeyWords(0, " ".join(keywords_main))
        self.text.SetKeyWords(1, " ".join(keywords_main2))
        self.text.SetKeyWords(2, " ".join(keywords_main3))
        self.text.SetKeyWords(3, " ".join(keywords_main4))
        self.text.StyleSetSpec(wx.stc.STC_STYLE_DEFAULT,"fore:#000000,back:#FFFFFF,face:%s,size:%d" % (self.main_font,int(self.fsg))) 
        self.text.StyleSetSpec(wx.stc.STC_LUA_DEFAULT,"fore:#000000,back:#FFFFFF,face:%s,size:%d" % (self.main_font,int(self.fsg))) 
        self.text.SetMarginType(3, wx.stc.STC_MARGIN_SYMBOL)
        self.text.SetMarginMask(3, wx.stc.STC_MASK_FOLDERS)
        self.text.StyleClearAll()
        ######################################################isotropic paramete highlight#####################################################################    
        self.text.IndicatorSetStyle(0, wx.stc.STC_INDIC_ROUNDBOX)
        self.text.IndicatorSetForeground(0, wx.Colour(255,255,0))       #yellow      
        self.text.IndicatorSetStyle(1, wx.stc.STC_INDIC_ROUNDBOX)
        self.text.IndicatorSetForeground(1, wx.Colour(255,0,0))
        self.text.IndicatorSetStyle(2, wx.stc.STC_INDIC_ROUNDBOX)       #blue
        self.text.IndicatorSetForeground(2, "#4876FF")
        if wx.VERSION > (2, 9, 0, 0):
            self.text.IndicatorSetAlpha(2, 60)
            self.text.IndicatorSetAlpha(1, 60)
            self.text.IndicatorSetAlpha(0, 60)
        self.text.StyleSetSpec(wx.stc.STC_LUA_WORD,"fore:#221dff,back:#FFFFFF,face:%s,size:%d"%(self.main_font,int(self.fsg)))
        self.text.StyleSetSpec(wx.stc.STC_LUA_WORD2,"fore:#ec0e0e,back:#FFFFFF,face:%s,size:%d"%(self.main_font,int(self.fsg)))
        self.text.StyleSetSpec(wx.stc.STC_LUA_WORD3,"fore:#221dff,back:#FFFFFF,face:%s,size:%d"%(self.main_font,int(self.fsg)))
        self.text.StyleSetSpec(wx.stc.STC_LUA_WORD4,"fore:#ec0e0e,back:#FFFFFF,face:%s,size:%d"%(self.main_font,int(self.fsg))) 