
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
#import wxversion
#print (wxversion.getInstalled())
#try:
#    import wx
#except ImportError, msg:
#    raise ImportError ('%s (need to run "sudo apt-get install python-wxgtk2.8" or install wxpython package for windows)' % (msg))
##import wx.html
import os
import sys

import wx.stc


class stcwindow(wx.stc.StyledTextCtrl):
#===============================================================================
#-------------------------------------------------------------------------------
    def __init__(self, parent, fsg, main_font,
                 id=-1, pos=wx.DefaultPosition,size=wx.DefaultSize, style=wx.TE_MULTILINE|wx.NO_BORDER|wx.WANTS_CHARS):
#-------------------------------------------------------------------------------
        """
        Create Editor instance.
        """
        wx.stc.StyledTextCtrl.__init__(self, parent, id, pos, size, style)
        self.SetCaretLineVisible(True)
        self.fsg=fsg
        self.main_font=main_font
        #font=wx.Font(13, wx.ROMAN, wx.NORMAL, wx.NORMAL, False, u'Arial')
        self.stclex()
        self.SetMarginSensitive(3, True)
        self.SetMarginWidth(3, 10)
        self.SetSelection(0, 0)
        self.SetBackSpaceUnIndents(True)
        self.CmdKeyClearAll()
        self.initKeyShortCut()
        self.SetSelBackground(True, wx.Colour(128,128,128))
        self.SetCaretLineBackground(wx.Colour(153,204,255)) 
        self.SetEdgeMode(wx.stc.STC_EDGE_LINE)
        self.SetEdgeColumn(80)
        self.SetEdgeColour(wx.LIGHT_GREY)
        # self.SetUseAntiAliasing(True)
        self.SetEOLMode(wx.stc.STC_EOL_CRLF)
        self.SetWrapMode(wx.stc.STC_WRAP_CHAR)
        self.WrapCount(2)
#        self.Colourise(0, -1)
    def convert_key(self, keydef):
        keylist = {
                'DOWN'  :wx.stc.STC_KEY_DOWN,
                'UP'    :wx.stc.STC_KEY_UP,
                'LEFT'  :wx.stc.STC_KEY_LEFT,
                'RIGHT' :wx.stc.STC_KEY_RIGHT,
                'HOME'  :wx.stc.STC_KEY_HOME,
                'END'   :wx.stc.STC_KEY_END,
                'PGUP'  :wx.stc.STC_KEY_PRIOR,
                'PGDN'  :wx.stc.STC_KEY_NEXT,
                'DEL'   :wx.stc.STC_KEY_DELETE,
                'INS'   :wx.stc.STC_KEY_INSERT,
                'ESC'   :wx.stc.STC_KEY_ESCAPE,
                'BACK'  :wx.stc.STC_KEY_BACK,
                'TAB'   :wx.stc.STC_KEY_TAB,
                'ENTER' :wx.stc.STC_KEY_RETURN,
                'PLUS'  :wx.stc.STC_KEY_ADD,
                '-'     :wx.stc.STC_KEY_SUBTRACT,
                '/'     :wx.stc.STC_KEY_DIVIDE,
            }
        f = 0
        ikey = 0
        for k in keydef.split('+'):
            uk = k.upper()
            if uk == 'CTRL':
                f |= wx.stc.STC_SCMOD_CTRL
            elif uk == 'ALT':
                f |= wx.stc.STC_SCMOD_ALT
            elif uk == 'SHIFT':
                f |= wx.stc.STC_SCMOD_SHIFT
            elif uk in keylist:
                ikey = keylist[uk]
            elif len(uk) == 1:
                ikey = ord(uk)
            else:
                error.error("[TextEditor] Undefined char [%s]" % uk)
                continue
        return f, ikey
    def stclex(self):
        from shelxlexer import lexer_class
        lexc=lexer_class(self, self.fsg, self.main_font)
    def initKeyShortCut(self):
        
        self.keydefs = {}
        action = [

#       wxSTC_CMD_BACKTAB Dedent the selected lines
            ('Shift+Tab', wx.stc.STC_CMD_BACKTAB),
#       wxSTC_CMD_CANCEL Cancel any modes such as call tip or auto-completion list display
            ('Esc', wx.stc.STC_CMD_CANCEL),
#       wxSTC_CMD_CHARLEFT Move caret left one character
            ('Left', wx.stc.STC_CMD_CHARLEFT),
#       wxSTC_CMD_CHARLEFTEXTEND Move caret left one character extending selection to new caret position
            ('Shift+Left', wx.stc.STC_CMD_CHARLEFTEXTEND),
#       wxSTC_CMD_CHARRIGHT Move caret right one character
            ('Right', wx.stc.STC_CMD_CHARRIGHT),
#       wxSTC_CMD_CHARRIGHTEXTEND Move caret right one character extending selection to new caret position
            ('Shift+Right', wx.stc.STC_CMD_CHARRIGHTEXTEND),
#       wxSTC_CMD_CLEAR
            ('Del', wx.stc.STC_CMD_CLEAR),
#       wxSTC_CMD_COPY Copy the selection to the clipboard
           ('Ctrl+C', wx.stc.STC_CMD_COPY),
           ('Ctrl+Ins', wx.stc.STC_CMD_COPY),
#       wxSTC_CMD_CUT Cut the selection to the clipboard
           ('Ctrl+X', wx.stc.STC_CMD_CUT),
           ('Shift+Del', wx.stc.STC_CMD_CUT),
#       wxSTC_CMD_DELETEBACK Delete the selection or if no selection, the character before the caret
           ('Back', wx.stc.STC_CMD_DELETEBACK),
#       wxSTC_CMD_DELETEBACKNOTLINE Delete the selection or if no selection, the character before the caret. Will not delete the character before at the start of a line.
#       wxSTC_CMD_DELWORDLEFT Delete the word to the left of the caret
            ('Ctrl+Back', wx.stc.STC_CMD_DELWORDLEFT),
#       wxSTC_CMD_DELWORDRIGHT Delete the word to the right of the caret
            ('Ctrl+Del', wx.stc.STC_CMD_DELWORDRIGHT),
#       wxSTC_CMD_DOCUMENTEND Move caret to last position in document
            ('End', wx.stc.STC_CMD_DOCUMENTEND),
#       wxSTC_CMD_DOCUMENTENDEXTEND Move caret to last position in document extending selection to new caret position
            ('Ctrl+Shift+End', wx.stc.STC_CMD_DOCUMENTENDEXTEND),
#       wxSTC_CMD_DOCUMENTSTART Move caret to first position in document
            ('Home', wx.stc.STC_CMD_DOCUMENTSTART),
#       wxSTC_CMD_DOCUMENTSTARTEXTEND Move caret to first position in document extending selection to new caret position
            ('Ctrl+Shift+Home', wx.stc.STC_CMD_DOCUMENTSTARTEXTEND),
#       wxSTC_CMD_EDITTOGGLEOVERTYPE Switch from insert to overtype mode or the reverse
            ('Ins', wx.stc.STC_CMD_EDITTOGGLEOVERTYPE),
#       wxSTC_CMD_FORMFEED Insert a Form Feed character
#       wxSTC_CMD_HOME Move caret to first position on line
#       wxSTC_CMD_HOMEDISPLAY Move caret to first position on display line
#           ('Shift+Home', wx.stc.STC_CMD_HOMEDISPLAY),
#       wxSTC_CMD_HOMEDISPLAYEXTEND Move caret to first position on display line extending selection to new caret position
#           ('Shift+Alt+Home', wx.stc.STC_CMD_HOMEDISPLAYEXTEND),
#       wxSTC_CMD_HOMEEXTEND Move caret to first position on line extending selection to new caret position
#       wxSTC_CMD_LINECUT Cut the line containing the caret
#            ('Ctrl+Shift+D', wx.stc.STC_CMD_LINECUT),
#       wxSTC_CMD_LINEDELETE Delete the line containing the caret
            #('Ctrl+D', wx.stc.STC_CMD_LINEDELETE),
#       wxSTC_CMD_LINEDOWN Move caret down one line
            ('Down', wx.stc.STC_CMD_LINEDOWN),
#       wxSTC_CMD_LINEDOWNEXTEND Move caret down one line extending selection to new caret position
            ('Shift+Down', wx.stc.STC_CMD_LINEDOWNEXTEND),
#       wxSTC_CMD_LINEEND Move caret to last position on line
#       wxSTC_CMD_LINEENDDISPLAY Move caret to last position on display line
            ('End', wx.stc.STC_CMD_LINEENDDISPLAY),
#       wxSTC_CMD_LINEENDDISPLAYEXTEND Move caret to last position on display line extending selection to new caret position
            ('Shift+End', wx.stc.STC_CMD_LINEENDDISPLAYEXTEND),
#       wxSTC_CMD_LINEENDEXTEND Move caret to last position on line extending selection to new caret position
#       wxSTC_CMD_LINESCROLLDOWN Scroll the document down, keeping the caret visible
            ('Ctrl+Down', wx.stc.STC_CMD_LINESCROLLDOWN),
#       wxSTC_CMD_LINESCROLLUP Scroll the document up, keeping the caret visible
            ('Ctrl+Up', wx.stc.STC_CMD_LINESCROLLUP),
#       wxSTC_CMD_LINETRANSPOSE Switch the current line with the previous
#            ('Alt+S', wx.stc.STC_CMD_LINETRANSPOSE),
#       wxSTC_CMD_LINEUP Move caret up one line
            ('Up', wx.stc.STC_CMD_LINEUP),
#       wxSTC_CMD_LINEUPEXTEND Move caret up one line extending selection to new caret position
            ('Shift+Up', wx.stc.STC_CMD_LINEUPEXTEND),
#       wxSTC_CMD_LOWERCASE Transform the selection to lower case
#           ('Ctrl+L', wx.stc.STC_CMD_LOWERCASE),
#       wxSTC_CMD_NEWLINE Insert a new line, may use a CRLF, CR or LF depending on EOL mode
            ('Enter', wx.stc.STC_CMD_NEWLINE),
#       wxSTC_CMD_PAGEDOWN Move caret one page down
            ('Pgdn', wx.stc.STC_CMD_PAGEDOWN),
#       wxSTC_CMD_PAGEDOWNEXTEND Move caret one page down extending selection to new caret position
            ('Shift+Pgdn', wx.stc.STC_CMD_PAGEDOWNEXTEND),
#       wxSTC_CMD_PAGEUP Move caret one page up
            ('Pgup', wx.stc.STC_CMD_PAGEUP),
#       wxSTC_CMD_PAGEUPEXTEND Move caret one page up extending selection to new caret position
            ('Shift+Pgup', wx.stc.STC_CMD_PAGEUPEXTEND),
            ('Ctrl+V', wx.stc.STC_CMD_PASTE),
            ('Shift+Ins', wx.stc.STC_CMD_PASTE),
#       wxSTC_CMD_REDO Redoes the next action on the undo history
#           ('Ctrl+Y', wx.stc.STC_CMD_REDO),
#       wxSTC_CMD_SELECTALL Select all the text in the document
#           ('Ctrl+A', wx.stc.STC_CMD_SELECTALL),
#       wxSTC_CMD_TAB If selection is empty or all on one line replace the selection with a tab character. If more than one line selected, indent the lines
            ('Tab', wx.stc.STC_CMD_TAB),
#       wxSTC_CMD_UNDO Redoes the next action on the undo history
#           ('Ctrl+Z', wx.stc.STC_CMD_UNDO),
#       wxSTC_CMD_UPPERCASE Transform the selection to upper case
#           ('Ctrl+U', wx.stc.STC_CMD_UPPERCASE),
#       wxSTC_CMD_VCHOME Move caret to before first visible character on line. If already there move to first character on line
            ('Home', wx.stc.STC_CMD_VCHOME),
#       wxSTC_CMD_VCHOMEEXTEND Like VCHome but extending selection to new caret position
            ('Shift+Home', wx.stc.STC_CMD_VCHOMEEXTEND),
#       wxSTC_CMD_WORDLEFT Move caret left one word
            ('Ctrl+Left', wx.stc.STC_CMD_WORDLEFT),
#       wxSTC_CMD_WORDLEFTEXTEND Move caret left one word extending selection to new caret position
            ('Ctrl+Shift+Left', wx.stc.STC_CMD_WORDLEFTEXTEND),
#       wxSTC_CMD_WORDRIGHT Move caret right one word
            ('Ctrl+Right', wx.stc.STC_CMD_WORDRIGHT),
#       wxSTC_CMD_WORDRIGHTEXTEND Move caret right one word extending selection to new caret position
            ('Ctrl+Shift+Right', wx.stc.STC_CMD_WORDRIGHTEXTEND),
#       wxSTC_CMD_ZOOMIN Magnify the displayed text by increasing the sizes by 1 point
#           ('Ctrl+B', wx.stc.STC_CMD_ZOOMIN),
#       wxSTC_CMD_ZOOMOUT Make the displayed text smaller by decreasing the sizes by 1 point
#           ('Ctrl+N', wx.stc.STC_CMD_ZOOMOUT),
#       wxSTC_CMD_DELLINELEFT: Use 2395 Delete back from the current position to the start of the line
            ('Alt+Back', wx.stc.STC_CMD_DELLINELEFT),
#       wxSTC_CMD_DELLINERIGHT: Use 2396 Delete forwards from the current position to the end of the line
            ('Alt+Del', wx.stc.STC_CMD_DELLINERIGHT),
#       wxSTC_CMD_WORDPARTLEFT: Use 2390 Move to the next change in capitalisation
            ('Alt+Left', wx.stc.STC_CMD_WORDPARTLEFT),
#       wxSTC_CMD_WORDPARTLEFTEXTEND: Use 2391 Move to the previous change in capitalisation extending selection to new caret position
            ('Alt+Shift+Left', wx.stc.STC_CMD_WORDPARTLEFTEXTEND),
#       wxSTC_CMD_WORDPARTRIGHT: Use 2392 Move caret right one word extending selection to new caret position
            ('Alt+Right', wx.stc.STC_CMD_WORDPARTRIGHT),
#       wxSTC_CMD_WORDPARTRIGHTEXTEND: Use 2393 Move to the next change in capitalisation extending selection to new caret position.
            ('Alt+Shift+Right', wx.stc.STC_CMD_WORDPARTRIGHTEXTEND),
        ]

        for keys, cmd in action:
            self.keydefs[keys.upper()] = cmd
            f, ikey = self.convert_key(keys)
            self.CmdKeyAssign(ikey, f, cmd)
