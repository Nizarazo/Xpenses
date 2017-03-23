class ZMixin:
    def render(self, s):
        resp = super().render(s)
        return "Z-{}-Z".format(resp)


class DuplicateMixin:
    def render(self, s):
        return super().render(s) * 3


class A:
    def render(self, s):
        return "A-{}-A".format(s)


class ZA(ZMixin, A):
    pass


class ZA3(DuplicateMixin, ZMixin, A):
    pass


class Z3A(ZMixin, DuplicateMixin, A):
    pass


o = ZA3()
print(o.render("shalom"))
o = Z3A()
print(o.render("shalom"))

#
# class B(A):
#     def render(self, s):
#         resp = super().render(s)
#         return "B-{}-B".format(resp)
#
#
# class ZB(ZMixin, B):
#     pass
#
#
# class C(B):
#     def render(self, s):
#         resp = super().render(s)
#         return "C-{}-C".format(resp)
#
#
# class ZC(ZMixin, C):
#     pass
#
#
# class H:
#     def render(self, s):
#         return "H-{}-H".format(s)
#
# class ZH(ZMixin, H):
#     pass
#
# class I(H):
#     def render(self, s):
#         resp = super().render(s)
#         return "I-{}-I".format(resp)
#
#
