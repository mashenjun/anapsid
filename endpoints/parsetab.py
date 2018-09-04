
# parsetab.py
# This file is automatically generated. Do not edit.
_tabversion = '3.2'

_lr_method = 'LALR'

_lr_signature = '\x9cVk\xb4\xea\xd1\xe8f~\xf1\xd0\xa4\xe4\xb2d\x18'
    
_lr_action_items = {'POINT':([5,6,7,8,9,11,],[-6,12,-9,-7,-8,-5,]),'PRED0':([2,5,6,7,8,9,11,],[8,-6,8,-9,-7,-8,-5,]),'PRED1':([2,5,6,7,8,9,11,],[9,-6,9,-9,-7,-8,-5,]),'URI':([0,1,2,4,5,6,7,8,9,10,11,12,],[2,-3,7,2,-6,7,-9,-7,-8,-2,-5,-4,]),'$end':([1,3,4,10,12,],[-3,0,-1,-2,-4,]),}

_lr_action = { }
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = { }
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'endpoints_list':([0,],[4,]),'predicate':([2,6,],[5,11,]),'endpoint':([0,4,],[1,10,]),'predicate_list':([2,],[6,]),'parse_sparql':([0,],[3,]),}

_lr_goto = { }
for _k, _v in _lr_goto_items.items():
   for _x,_y in zip(_v[0],_v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = { }
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> parse_sparql","S'",1,None,None,None),
  ('parse_sparql -> endpoints_list','parse_sparql',1,'p_parse_sparql','/Users/mashenjun/WorkSpace/anapsid/ANAPSID/Decomposer/parseEndpoints.py',29),
  ('endpoints_list -> endpoints_list endpoint','endpoints_list',2,'p_endpoints_list','/Users/mashenjun/WorkSpace/anapsid/ANAPSID/Decomposer/parseEndpoints.py',35),
  ('endpoints_list -> endpoint','endpoints_list',1,'p_single_endpoint_list','/Users/mashenjun/WorkSpace/anapsid/ANAPSID/Decomposer/parseEndpoints.py',41),
  ('endpoint -> URI predicate_list POINT','endpoint',3,'p_endpoint','/Users/mashenjun/WorkSpace/anapsid/ANAPSID/Decomposer/parseEndpoints.py',47),
  ('predicate_list -> predicate_list predicate','predicate_list',2,'p_predicate_list','/Users/mashenjun/WorkSpace/anapsid/ANAPSID/Decomposer/parseEndpoints.py',53),
  ('predicate_list -> predicate','predicate_list',1,'p_single_predicate_list','/Users/mashenjun/WorkSpace/anapsid/ANAPSID/Decomposer/parseEndpoints.py',59),
  ('predicate -> PRED0','predicate',1,'p_predicate_0','/Users/mashenjun/WorkSpace/anapsid/ANAPSID/Decomposer/parseEndpoints.py',65),
  ('predicate -> PRED1','predicate',1,'p_predicate_1','/Users/mashenjun/WorkSpace/anapsid/ANAPSID/Decomposer/parseEndpoints.py',71),
  ('predicate -> URI','predicate',1,'p_predicate_u','/Users/mashenjun/WorkSpace/anapsid/ANAPSID/Decomposer/parseEndpoints.py',77),
]
