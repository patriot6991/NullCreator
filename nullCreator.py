import maya.cmds as mc

class NullCreator(object):
    def __init__(self):
        self.pf = ''
        self.sf = '_null'
        self.nn = ''

    def original(*args):
        mc.text('t1', en=True, edit=True)
        mc.text('t2', en=True, edit=True)
        mc.text('t3', en=False, edit=True)
        mc.textField('f1', en=True, edit=True)
        mc.textField('f2', en=True, edit=True)
        mc.textField('f3', en=False, edit=True)

    def new(self, *args):
        mc.text('t1', en=False, edit=True)
        mc.text('t2', en=False, edit=True)
        mc.text('t3', en=True, edit=True)
        mc.textField('f1', en=False, edit=True)
        mc.textField('f2', en=False, edit=True)
        mc.textField('f3', en=True, edit=True)

    def ui(self):
        win = mc.window(title='nullCreator', widthHeight=(300,170))
        form = mc.formLayout()

        rc = mc.radioCollection()
        rb1 = mc.radioButton(l='Original Name', sl=True, onc=self.original)
        rb2 = mc.radioButton(l='New Name', onc=self.new)
        t1 = mc.text('t1', l='Prefix :', w=50,  h=20, al='right', en=True)
        t2 = mc.text('t2', l='Suffix :', w=50,  h=20, al='right', en=True)
        t3 = mc.text('t3', l='Name :', w=50, h=20, al='right', en=False)
        f1 = mc.textField('f1', w=225, h=20, text=self.pf, en=True)
        f2 = mc.textField('f2', w=225, h=20, text=self.sf, en=True)
        f3 = mc.textField('f3', w=225, h=20, text=self.nn, en=False)
        sp = mc.separator(w=280)
        b1 = mc.button(l='Create', w=280, h=40)

        mc.formLayout(form, edit=True, attachForm=[
            (rb1,'top',10),(rb1,'left',30),
            (rb2, 'top', 10), (rb2, 'left', 160),
            (t1,'top',35),(t1,'left',10),
            (t2,'top',60),(t2,'left',10),
            (t3,'top',90),(t3,'left',10),
            (f1,'top',35),(f1,'left',65),
            (f2,'top',60),(f2,'left',65),
            (f3,'top',90),(f3,'left',65),
            (sp,'top',85),(sp,'left',10),
            (b1,'top',120),(b1,'left',10)
        ])

        mc.showWindow(win)

a = NullCreator()
a.ui()
