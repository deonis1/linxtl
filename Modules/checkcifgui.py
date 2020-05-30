#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import wx


class checkcifgui(wx.Dialog):
    def __init__(self, parent, version, fnoe, dirname, path, text):
        wx.Dialog.__init__(self, parent, style=wx.DEFAULT_DIALOG_STYLE | wx.RESIZE_BORDER)
        # begin wxGlade: checkcifgui.__init__
        ###############################################################
        self.SetSize((1061, 584))
        self.user_list = wx.ListBox(self, wx.ID_ANY, choices=[], style=wx.LB_HSCROLL | wx.LB_SINGLE)
        colors = ["Yellow", "Colourless", "Black", "Pink", "Purple", "Orange", "Grey", "White", "Green", "Red", "Blue",
                  "Aqua", "Brown"]
        shapes = ["block", "prism", "needle", "cube", "sphere", "plate"]
        crystal_family = ["Triclinic", "Monoclinic", "Orthorombic", "Tetragonal", "Hexagonal", "Cubic"]
        self.colours = wx.ComboBox(self, wx.ID_ANY, choices=colors, style=wx.CB_DROPDOWN)
        self.crystalshape = wx.ComboBox(self, wx.ID_ANY, choices=shapes, style=wx.CB_DROPDOWN)
        self.moiety = wx.TextCtrl(self, wx.ID_ANY, "")
        self.xsize = wx.TextCtrl(self, wx.ID_ANY, "")
        self.ysize = wx.TextCtrl(self, wx.ID_ANY, "")
        self.zsize = wx.TextCtrl(self, wx.ID_ANY, "")
        self.valcellsetting = wx.ComboBox(self, wx.ID_ANY, choices=crystal_family, style=wx.CB_DROPDOWN)
        self.spacehm = wx.TextCtrl(self, wx.ID_ANY, "")
        self.zsetting = wx.TextCtrl(self, wx.ID_ANY, "")
        self.abs_min = wx.TextCtrl(self, wx.ID_ANY, "")
        self.abs_max = wx.TextCtrl(self, wx.ID_ANY, "")
        self.valtemp = wx.TextCtrl(self, wx.ID_ANY, "")
        self.valhtreat = wx.TextCtrl(self, wx.ID_ANY, "")
        self.instrumentsettings = wx.ComboBox(self, wx.ID_ANY, choices=[], style=wx.CB_DROPDOWN)
        self.okay = wx.Button(self, wx.ID_ANY, ("OK"))
        self.cancel = wx.Button(self, wx.ID_CANCEL, ("Cancel"))

        self.__set_properties()
        self.__do_layout()
        # end wxGlade

    def __set_properties(self):
        # begin wxGlade: checkcifgui.__set_properties
        self.SetTitle(("Prepare cif for publication"))
        self.user_list.SetMinSize((200, 197))
        self.colours.SetMinSize((200, -1))
        self.crystalshape.SetMinSize((200, -1))
        self.moiety.SetMinSize((200, -1))
        self.xsize.SetMinSize((150, -1))
        self.ysize.SetMinSize((150, -1))
        self.zsize.SetMinSize((150, -1))
        self.valcellsetting.SetMinSize((200, -1))
        self.spacehm.SetMinSize((150, -1))
        self.zsetting.SetMinSize((150, -1))
        self.abs_min.SetMinSize((150, -1))
        self.abs_max.SetMinSize((150, -1))
        self.valtemp.SetMinSize((150, -1))
        self.valhtreat.SetMinSize((150, -1))
        self.instrumentsettings.SetMinSize((200, -1))
        self.okay.SetDefault()
        self.cancel.SetDefault()
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: checkcifgui.__do_layout
        main_sizer1 = wx.BoxSizer(wx.VERTICAL)
        main_sizer2 = wx.BoxSizer(wx.VERTICAL)
        footer = wx.GridSizer(1, 2, 0, 0)
        main_panel = wx.BoxSizer(wx.HORIZONTAL)
        parameters_sizer = wx.BoxSizer(wx.HORIZONTAL)
        other_setting_sizer = wx.StaticBoxSizer(wx.StaticBox(self, wx.ID_ANY, ("Other Settings")), wx.VERTICAL)
        othersetting_gsizer = wx.FlexGridSizer(5, 2, 15, 10)
        crystal_setting_sizer = wx.StaticBoxSizer(wx.StaticBox(self, wx.ID_ANY, ("Crystal Setting")), wx.VERTICAL)
        crystalsetting_gsizer = wx.FlexGridSizer(9, 2, 10, 10)
        main_panel.Add(self.user_list, 0, wx.ALL | wx.EXPAND, 10)
        colour = wx.StaticText(self, wx.ID_ANY, ("Colour:"))
        crystalsetting_gsizer.Add(colour, 0, wx.ALIGN_CENTER_VERTICAL, 0)
        crystalsetting_gsizer.Add(self.colours, 0, wx.ALIGN_CENTER_VERTICAL, 0)
        ylabel_copy = wx.StaticText(self, wx.ID_ANY, ("Crystal shape:"))
        crystalsetting_gsizer.Add(ylabel_copy, 0, wx.ALIGN_CENTER_VERTICAL, 0)
        crystalsetting_gsizer.Add(self.crystalshape, 0, wx.ALIGN_CENTER_VERTICAL, 0)
        lmoiety = wx.StaticText(self, wx.ID_ANY, ("Moiety Formula"))
        crystalsetting_gsizer.Add(lmoiety, 0, wx.ALIGN_CENTER_VERTICAL, 0)
        crystalsetting_gsizer.Add(self.moiety, 0, wx.ALIGN_CENTER_VERTICAL, 0)
        xlabel = wx.StaticText(self, wx.ID_ANY, ("Size min, mm:"))
        crystalsetting_gsizer.Add(xlabel, 0, wx.ALIGN_CENTER_VERTICAL, 0)
        crystalsetting_gsizer.Add(self.xsize, 0, wx.ALIGN_CENTER_VERTICAL, 0)
        ylabel = wx.StaticText(self, wx.ID_ANY, ("Size mid, mm:"))
        crystalsetting_gsizer.Add(ylabel, 0, wx.ALIGN_CENTER_VERTICAL, 0)
        crystalsetting_gsizer.Add(self.ysize, 0, wx.ALIGN_CENTER_VERTICAL, 0)
        zlabel = wx.StaticText(self, wx.ID_ANY, ("Size max, mm:"))
        crystalsetting_gsizer.Add(zlabel, 0, wx.ALIGN_CENTER_VERTICAL, 0)
        crystalsetting_gsizer.Add(self.zsize, 0, wx.ALIGN_CENTER_VERTICAL, 0)
        cellsetting = wx.StaticText(self, wx.ID_ANY, ("Cell setting:"))
        crystalsetting_gsizer.Add(cellsetting, 0, wx.ALIGN_CENTER_VERTICAL, 0)
        crystalsetting_gsizer.Add(self.valcellsetting, 0, wx.ALIGN_CENTER_VERTICAL, 0)
        spacegp = wx.StaticText(self, wx.ID_ANY, ("Space Group H-M:"))
        crystalsetting_gsizer.Add(spacegp, 0, wx.ALIGN_CENTER_VERTICAL, 0)
        crystalsetting_gsizer.Add(self.spacehm, 0, wx.ALIGN_CENTER_VERTICAL, 0)
        znum = wx.StaticText(self, wx.ID_ANY, ("Z:"))
        crystalsetting_gsizer.Add(znum, 0, wx.ALIGN_CENTER_VERTICAL, 0)
        crystalsetting_gsizer.Add(self.zsetting, 0, wx.ALIGN_CENTER_VERTICAL, 0)
        crystal_setting_sizer.Add(crystalsetting_gsizer, 1, wx.ALL | wx.EXPAND, 10)
        parameters_sizer.Add(crystal_setting_sizer, 1, wx.ALL | wx.EXPAND, 10)
        absmin = wx.StaticText(self, wx.ID_ANY, ("abs_T_min:"))
        othersetting_gsizer.Add(absmin, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 0)
        othersetting_gsizer.Add(self.abs_min, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 0)
        absmax = wx.StaticText(self, wx.ID_ANY, ("abs_T_max:"))
        othersetting_gsizer.Add(absmax, 0, wx.ALIGN_CENTER_VERTICAL, 0)
        othersetting_gsizer.Add(self.abs_max, 0, wx.ALIGN_CENTER_VERTICAL, 0)
        ltemp = wx.StaticText(self, wx.ID_ANY, ("Temperature, K:"))
        othersetting_gsizer.Add(ltemp, 0, wx.ALIGN_CENTER_VERTICAL, 0)
        othersetting_gsizer.Add(self.valtemp, 0, wx.ALIGN_CENTER_VERTICAL, 0)
        hlabel_copy = wx.StaticText(self, wx.ID_ANY, ("Hydrogen Treatment:"))
        othersetting_gsizer.Add(hlabel_copy, 0, wx.ALIGN_CENTER_VERTICAL, 0)
        othersetting_gsizer.Add(self.valhtreat, 0, wx.ALIGN_CENTER_VERTICAL, 0)
        instrument = wx.StaticText(self, wx.ID_ANY, ("Instrument setting:"))
        othersetting_gsizer.Add(instrument, 0, wx.ALIGN_CENTER_VERTICAL, 0)
        othersetting_gsizer.Add(self.instrumentsettings, 0, wx.ALIGN_CENTER_VERTICAL, 0)
        other_setting_sizer.Add(othersetting_gsizer, 1, wx.ALL | wx.EXPAND, 10)
        parameters_sizer.Add(other_setting_sizer, 1, wx.ALL | wx.EXPAND, 10)
        main_panel.Add(parameters_sizer, 1, wx.EXPAND, 0)
        main_sizer2.Add(main_panel, 5, wx.EXPAND, 0)
        footer.Add(self.okay, 0, wx.ALIGN_CENTER, 0)
        footer.Add(self.cancel, 0, wx.ALIGN_CENTER | wx.ALL, 10)
        main_sizer2.Add(footer, 1, wx.ALIGN_CENTER | wx.EXPAND, 0)
        main_sizer1.Add(main_sizer2, 1, wx.EXPAND, 0)
        self.SetSizer(main_sizer1)
        self.Layout()
        self.Centre()
        # end wxGlade

    def get_values(self):
        values = {"_chemical_formula_moiety": self.moiety.GetValue(), "_exptl_crystal_colour": "'"+self.colours.GetValue()+"'",
                  "_exptl_crystal_description": "'"+self.crystalshape.GetValue()+"'",
                  "_exptl_crystal_size_min": self.xsize.GetValue(),
                  "_exptl_crystal_size_mid": self.ysize.GetValue(), "_exptl_crystal_size_max": self.zsize.GetValue(),
                  "_space_group_crystal_system": "'"+self.valcellsetting.GetValue()+"'",
                  "_space_group_name_Hall": "'"+self.spacehm.GetValue()+"'", "_cell_formula_units_Z": self.zsetting.GetValue(),
                  "_exptl_absorpt_correction_T_min": self.abs_min.GetValue(),
                  "_exptl_absorpt_correction_T_max": self.abs_max.GetValue(),
                  "_diffrn_ambient_temperature": self.valtemp.GetValue(),
                  "_refine_ls_hydrogen_treatment": "'"+self.valhtreat.GetValue()+"'",
                  "user": self.user_list.GetStringSelection(),  "dev_default": self.instrumentsettings.GetValue()}

        # # print"lastposition ", self.lastposition1, self.lastposition2
        #  lintmp=open(os.path.join(self.dirname,"lin.tmp"), 'w')
        #  lintmp.writelines(self.lastposition1+'\n' + self.lastposition2+"\n"+str(listbsel))
        #  lintmp.close()

        return values

    def set_values(self, values):
        self.user_list.InsertItems(values["userlist"], 0)
        self.user_list.SetStringSelection(str(values["user"]))
        self.instrumentsettings.SetItems(values["dev"])
        self.instrumentsettings.SetValue(values["dev_default"])
        self.moiety.SetValue(values["_chemical_formula_moiety"])
        self.colours.SetValue(values["_exptl_crystal_colour"])
        self.crystalshape.SetValue(values["_exptl_crystal_description"])
        self.xsize.SetValue(values["_exptl_crystal_size_min"])
        self.ysize.SetValue(values["_exptl_crystal_size_mid"])
        self.zsize.SetValue(values["_exptl_crystal_size_max"])
        self.valcellsetting.SetValue(values["_space_group_crystal_system"])
        self.spacehm.SetValue(values["_space_group_name_Hall"])
        self.zsetting.SetValue(values["_cell_formula_units_Z"])
        self.abs_min.SetValue(values["_exptl_absorpt_correction_T_min"])
        self.abs_max.SetValue(values["_exptl_absorpt_correction_T_max"])
        self.valtemp.SetValue(values["_diffrn_ambient_temperature"])
        self.valhtreat.SetValue(values["_refine_ls_hydrogen_treatment"])
