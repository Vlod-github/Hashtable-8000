

def get_base(struct: str) -> str:
	return f'''
library H8k
	globals
		private hashtable H = InitHashtable()
		private integer current = 0
		private integer max = 0
		private integer array pointers
	endglobals
	private function new takes nothing returns integer
		local integer this = current
		if current == 0 then
			set max = max + 1
			set this = max
			if this > 8190 then
				return 0
			endif
		else
			set current = pointers[this]
		endif
		set pointers[this] = -1
		return this
	endfunction
	private function delete takes integer this returns nothing
		if this <= 0 or pointers[this] != -1 then
			return
		endif
		set pointers[this] = current
		set current = this
		call FlushChildHashtable(H, this)
	endfunction
{struct}
endlibrary
'''


def get_struct(typ: str, LOADSAVE: str, REMOVE: str) -> str:
	return f'''
struct h8k_{typ}
	static method create takes nothing returns h8k_{typ}
		return new()
	endmethod
	method operator [] takes integer i returns {typ}
		return Load{LOADSAVE}(H,this,i)
	endmethod
	method operator []= takes integer i, {typ} val returns nothing
		call Save{LOADSAVE}(H,this,i,val)
	endmethod
	method remove takes integer i returns nothing
		call RemoveSaved{REMOVE}(H,this,i)
	endmethod
	method destroy takes nothing returns nothing
		call delete(this)
	endmethod
endstruct
'''

if __name__ == "__main__":
	path_code = 'H8k.vjass'
	code = get_struct('boolean', 'Boolean', 'Boolean')
	code += get_struct('string', 'Str', 'String')
	code += get_struct('destructable', 'DestructableHandle', 'Handle')
	code += get_struct('effect', 'EffectHandle', 'Handle')
	code += get_struct('integer', 'Integer', 'Integer')
	code += get_struct('item', 'ItemHandle', 'Handle')
	code += get_struct('lightning', 'LightningHandle', 'Handle')
	code += get_struct('multiboard', 'MultiboardHandle', 'Handle')
	code += get_struct('multiboarditem', 'MultiboardItemHandle', 'Handle')
	code += get_struct('player', 'PlayerHandle', 'Handle')
	code += get_struct('real', 'Real', 'Real')
	code += get_struct('rect', 'RectHandle', 'Handle')
	code += get_struct('region', 'RegionHandle', 'Handle')
	code += get_struct('timer', 'TimerHandle', 'Handle')
	code += get_struct('trigger', 'TriggerHandle', 'Handle')
	code += get_struct('unit', 'UnitHandle', 'Handle')

	with open(path_code, 'w') as f:
		f.write(get_base(code))