instructions = {

    0X00: 'NOP',
    0X01: 'LD BC,D16',
    0X02: 'LD (BC),A',
    0x03: 'INC BC',
    0x04: 'INC B',
    0x05: 'DEC B',
    0X06: 'LD B,D8',
    0X07: 'RLCA',
    0X08: 'LD (A16),SP',
    0X09: 'ADD HL,BC',
    0X0A: 'LD A,(BC)',
    0X0B: 'DEC BC',
    0X0C: 'INC C',
    0X0D: 'DEC C',
    0X0E: 'LD C,D8',
    0X0F: 'RRCA',

    0X10: 'STOP',
    0X11: 'LD DE,D16',
    0X12: 'LD (DE),A',
    0X13: 'INC DE',
    0X14: 'INC D',
    0X15: 'DEC D',
    0X16: 'LD D,D8',
    0X17: 'RLA',
    0X18: 'JR PC+R8',
    0X19: 'ADD HL,DE',
    0X1A: 'LD A,(DE)',
    0X1B: 'DEC DE',
    0X1C: 'INC E',
    0X1D: 'DEC E',
    0X1E: 'LD E,D8',
    0X1F: 'RRA',

    0X20: 'JR NZ,PC+R8',
    0X21: 'LD HL,D16',
    0X22: 'LD (HL+),A',
    0X23: 'INC HL',
    0X24: 'INC H',
    0X25: 'DEC H',
    0X26: 'LD H,D8',
    0X27: 'DAA',
    0X28: 'JR Z,PC+R8',
    0X29: 'ADD HL,HL',
    0X2A: 'LD A,(HL+)',
    0X2B: 'DEC HL',
    0X2C: 'INC L',
    0X2D: 'DEC L',
    0X2E: 'LD L,D8',
    0X2F: 'CPL',

    0X30: 'JR NC,PC+R8',
    0X31: 'LD SP,D16',
    0X32: 'LD (HL-),A',
    0X33: 'INC SP',
    0X34: 'INC (HL)',
    0X35: 'DEC (HL)',
    0X36: 'LD (HL),D8',
    0X37: 'SCF',
    0X38: 'JR C,PC+R8',
    0X39: 'ADD HL,SP',
    0X3A: 'LD A,(HL-)',
    0X3B: 'DEC SP',
    0X3C: 'INC A',
    0X3D: 'DEC A',
    0X3E: 'LD A,D8',
    0X3F: 'CCF',

    0X40: 'LD B,B',
    0X41: 'LD B,C',
    0X42: 'LD B,D',
    0X43: 'LD B,E',
    0X44: 'LD B,H',
    0X45: 'LD B,L',
    0X46: 'LD B,(HL)',
    0X47: 'LD B,A',
    0X48: 'LD C,B',
    0X49: 'LD C,C',
    0X4A: 'LD C,D',
    0X4B: 'LD C,E',
    0X4C: 'LD C,H',
    0X4D: 'LD C,L',
    0X4E: 'LD C,(HL)',
    0X4F: 'LD C,A',

    0X50: 'LD D,B',
    0X51: 'LD D,C',
    0X52: 'LD D,D',
    0X53: 'LD D,E',
    0X54: 'LD D,H',
    0X55: 'LD D,L',
    0X56: 'LD D,(HL)',
    0X57: 'LD D,A',
    0X58: 'LD E,B',
    0X59: 'LD E,C',
    0X5A: 'LD E,D',
    0X5B: 'LD E,E',
    0X5C: 'LD E,H',
    0X5D: 'LD E,L',
    0X5E: 'LD E,(HL)',
    0X5F: 'LD E,A',

    0X60: 'LD H,B',
    0X61: 'LD H,C',
    0X62: 'LD H,D',
    0X63: 'LD H,E',
    0X64: 'LD H,H',
    0X65: 'LD H,L',
    0X66: 'LD H,(HL)',
    0X67: 'LD H,A',
    0X68: 'LD L,B',
    0X69: 'LD L,C',
    0X6A: 'LD L,D',
    0X6B: 'LD L,E',
    0X6C: 'LD L,H',
    0X6D: 'LD L,L',
    0X6E: 'LD L,(HL)',
    0X6F: 'LD L,A',

    0X70: 'LD (HL),B',
    0X71: 'LD (HL),C',
    0X72: 'LD (HL),D',
    0X73: 'LD (HL),E',
    0X74: 'LD (HL),H',
    0X75: 'LD (HL),L',
    0X76: 'HALT',
    0X77: 'LD (HL),A',
    0X78: 'LD A,B',
    0X79: 'LD A,C',
    0X7A: 'LD A,D',
    0X7B: 'LD A,E',
    0X7C: 'LD A,H',
    0X7D: 'LD A,L',
    0X7E: 'LD A,(HL)',
    0X7F: 'LD A,A',

    0X80: 'ADD B',
    0X81: 'ADD C',
    0X82: 'ADD D',
    0X83: 'ADD E',
    0X84: 'ADD H',
    0X85: 'ADD L',
    0X86: 'ADD (HL)',
    0X87: 'ADD A',
    0X88: 'ADC B',
    0X89: 'ADC C',
    0X8A: 'ADC D',
    0X8B: 'ADC E',
    0X8C: 'ADC H',
    0X8D: 'ADC L',
    0X8E: 'ADC (HL)',
    0X8F: 'ADC A',    

    0X90: 'SUB B',
    0X91: 'SUB C',
    0X92: 'SUB D',
    0X93: 'SUB E',
    0X94: 'SUB H',
    0X95: 'SUB L',
    0X96: 'SUB (HL)',
    0X97: 'SUB A',
    0X98: 'SBC B',
    0X99: 'SBC C',
    0X9A: 'SBC D',
    0X9B: 'SBC E',
    0X9C: 'SBC H',
    0X9D: 'SBC L',
    0X9E: 'SBC (HL)',
    0X9F: 'SBC A',

    0XA0: 'AND B',
    0XA1: 'AND C',
    0XA2: 'AND D',
    0XA3: 'AND E',
    0XA4: 'AND H',
    0XA5: 'AND L',
    0XA6: 'AND (HL)',
    0XA7: 'AND A',
    0XA8: 'XOR B',
    0XA9: 'XOR C',
    0XAA: 'XOR D',
    0XAB: 'XOR E',
    0XAC: 'XOR H',
    0XAD: 'XOR L',
    0XAE: 'XOR (HL)',
    0XAF: 'XOR A',

    0XB0: 'OR B',
    0XB1: 'OR C',
    0XB2: 'OR D',
    0XB3: 'OR E',
    0XB4: 'OR H',
    0XB5: 'OR L',
    0XB6: 'OR (HL)',
    0XB7: 'OR A',
    0XB8: 'CP B',
    0XB9: 'CP C',
    0XBA: 'CP D',
    0XBB: 'CP E',
    0XBC: 'CP H',
    0XBD: 'CP L',
    0XBE: 'CP (HL)',
    0XBF: 'CP A',

    0XC0: 'RET NZ',
    0XC1: 'POP BC',
    0XC2: 'JP NZ,A16',
    0XC3: 'JP A16',
    0XC4: 'CALL NZ,A16',
    0XC5: 'PUSH BC',
    0XC6: 'ADD D8',
    0XC7: 'RST $00',
    0XC8: 'RET Z',
    0XC9: 'RET',
    0XCA: 'JP Z,A16',
    0XCB: 'CBPREFIX',
    0XCC: 'CALL Z,A16',
    0XCD: 'CALL A16',
    0XCE: 'ADC D8',
    0XCF: 'RST $08',

    0XD0: 'RET NC',
    0XD1: 'POP DE',
    0XD2: 'JP NC,A16',
    0XD3: 'DB $D3',
    0XD4: 'CALL NC,A16',
    0XD5: 'PUSH DE',
    0XD6: 'SUB D8',
    0XD7: 'RST $10',
    0XD8: 'RET C',
    0XD9: 'RETI',
    0XDA: 'JP C,A16',
    0XDB: 'DB $DB',
    0XDC: 'CALL C,A16',
    0XDD: 'DB $DD',
    0XDE: 'SBC D8',
    0XDF: 'RST $18',

    0XE0: 'LDH (A8),A',
    0XE1: 'POP HL',
    0XE2: 'LD (C),A',
    0XE3: 'DB $E3',
    0XE4: 'DB $E4',
    0XE5: 'PUSH HL',
    0XE6: 'AND D8',
    0XE7: 'RST $20',
    0XE8: 'ADD SP,R8',
    0XE9: 'JP HL',
    0XEA: 'LD (A16),A',
    0XEB: 'DB $EB',
    0XEC: 'DB $EC',
    0XED: 'DB $ED',
    0XEE: 'XOR D8',
    0XEF: 'RST $28',

    0XF0: 'LDH A,(A8)',
    0XF1: 'POP AF',
    0XF2: 'LD A,(C)',
    0XF3: 'DI',
    0XF4: 'DB $F4',
    0XF5: 'PUSH AF',
    0XF6: 'OR D8',
    0XF7: 'RST $30',
    0XF8: 'LD HL,SP+R8',
    0XF9: 'LD SP,HL',
    0XFA: 'LD A,(A16)',
    0XFB: 'EI',
    0XFC: 'DB $FC',
    0XFD: 'DB $FD',
    0XFE: 'CP D8',
    0XFF: 'RST $38',

}

cb_instructions = {
    
    0X00: 'RLC B',
    0X01: 'RLC C',
    0X02: 'RLC D',
    0X03: 'RLC E',
    0X04: 'RLC H',
    0X05: 'RLC L',
    0X06: 'RLC (HL)',
    0X07: 'RLC A',
    0X08: 'RRC B',
    0X09: 'RRC C',
    0X0A: 'RRC D',
    0X0B: 'RRC E',
    0X0C: 'RRC H',
    0X0D: 'RRC L',
    0X0E: 'RRC (HL)',
    0X0F: 'RRC A',
    
    0X10: 'RL B',
    0X11: 'RL C',
    0X12: 'RL D',
    0X13: 'RL E',
    0X14: 'RL H',
    0X15: 'RL L',
    0X16: 'RL (HL)',
    0X17: 'RL A',
    0X18: 'RR B',
    0X19: 'RR C',
    0X1A: 'RR D',
    0X1B: 'RR E',
    0X1C: 'RR H',
    0X1D: 'RR L',
    0X1E: 'RR (HL)',
    0X1F: 'RR A',
    
    0X20: 'SLA B',
    0X21: 'SLA C',
    0X22: 'SLA D',
    0X23: 'SLA E',
    0X24: 'SLA H',
    0X25: 'SLA L',
    0X26: 'SLA (HL)',
    0X27: 'SLA A',
    0X28: 'SRA B',
    0X29: 'SRA C',
    0X2A: 'SRA D',
    0X2B: 'SRA E',
    0X2C: 'SRA H',
    0X2D: 'SRA L',
    0X2E: 'SRA (HL)',
    0X2F: 'SRA A',
    
    0X30: 'SWAP B',
    0X31: 'SWAP C',
    0X32: 'SWAP D',
    0X33: 'SWAP E',
    0X34: 'SWAP H',
    0X35: 'SWAP L',
    0X36: 'SWAP (HL)',
    0X37: 'SWAP A',
    0X38: 'SRL B',
    0X39: 'SRL C',
    0X3A: 'SRL D',
    0X3B: 'SRL E',
    0X3C: 'SRL H',
    0X3D: 'SRL L',
    0X3E: 'SRL (HL)',
    0X3F: 'SRL A',
    
    0X40: 'BIT 0,B',
    0X41: 'BIT 0,C',
    0X42: 'BIT 0,D',
    0X43: 'BIT 0,E',
    0X44: 'BIT 0,H',
    0X45: 'BIT 0,L',
    0X46: 'BIT 0,(HL)',
    0X47: 'BIT 0,A',
    0X48: 'BIT 1,B',
    0X49: 'BIT 1,C',
    0X4A: 'BIT 1,D',
    0X4B: 'BIT 1,E',
    0X4C: 'BIT 1,H',
    0X4D: 'BIT 1,L',
    0X4E: 'BIT 1,(HL)',
    0X4F: 'BIT 1,A',
    
    0X50: 'BIT 2,B',
    0X51: 'BIT 2,C',
    0X52: 'BIT 2,D',
    0X53: 'BIT 2,E',
    0X54: 'BIT 2,H',
    0X55: 'BIT 2,L',
    0X56: 'BIT 2,(HL)',
    0X57: 'BIT 2,A',
    0X58: 'BIT 3,B',
    0X59: 'BIT 3,C',
    0X5A: 'BIT 3,D',
    0X5B: 'BIT 3,E',
    0X5C: 'BIT 3,H',
    0X5D: 'BIT 3,L',
    0X5E: 'BIT 3,(HL)',
    0X5F: 'BIT 3,A',
    
    0X60: 'BIT 4,B',
    0X61: 'BIT 4,C',
    0X62: 'BIT 4,D',
    0X63: 'BIT 4,E',
    0X64: 'BIT 4,H',
    0X65: 'BIT 4,L',
    0X66: 'BIT 4,(HL)',
    0X67: 'BIT 4,A',
    0X68: 'BIT 5,B',
    0X69: 'BIT 5,C',
    0X6A: 'BIT 5,D',
    0X6B: 'BIT 5,E',
    0X6C: 'BIT 5,H',
    0X6D: 'BIT 5,L',
    0X6E: 'BIT 5,(HL)',
    0X6F: 'BIT 5,A',

    0X70: 'BIT 6,B',
    0X71: 'BIT 6,C',
    0X72: 'BIT 6,D',
    0X73: 'BIT 6,E',
    0X74: 'BIT 6,H',
    0X75: 'BIT 6,L',
    0X76: 'BIT 6,(HL)',
    0X77: 'BIT 6,A',
    0X78: 'BIT 7,B',
    0X79: 'BIT 7,C',
    0X7A: 'BIT 7,D',
    0X7B: 'BIT 7,E',
    0X7C: 'BIT 7,H',
    0X7D: 'BIT 7,L',
    0X7E: 'BIT 7,(HL)',
    0X7F: 'BIT 7,A', 

    0X80: 'RES 0,B',
    0X81: 'RES 0,C',
    0X82: 'RES 0,D',
    0X83: 'RES 0,E',
    0X84: 'RES 0,H',
    0X85: 'RES 0,L',
    0X86: 'RES 0,(HL)',
    0X87: 'RES 0,A',
    0X88: 'RES 1,B',
    0X89: 'RES 1,C',
    0X8A: 'RES 1,D',
    0X8B: 'RES 1,E',
    0X8C: 'RES 1,H',
    0X8D: 'RES 1,L',
    0X8E: 'RES 1,(HL)',
    0X8F: 'RES 1,A',
    
    0X90: 'RES 2,B',
    0X91: 'RES 2,C',
    0X92: 'RES 2,D',
    0X93: 'RES 2,E',
    0X94: 'RES 2,H',
    0X95: 'RES 2,L',
    0X96: 'RES 2,(HL)',
    0X97: 'RES 2,A',
    0X98: 'RES 3,B',
    0X99: 'RES 3,C',
    0X9A: 'RES 3,D',
    0X9B: 'RES 3,E',
    0X9C: 'RES 3,H',
    0X9D: 'RES 3,L',
    0X9E: 'RES 3,(HL)',
    0X9F: 'RES 3,A',
    
    0XA0: 'RES 4,B',
    0XA1: 'RES 4,C',
    0XA2: 'RES 4,D',
    0XA3: 'RES 4,E',
    0XA4: 'RES 4,H',
    0XA5: 'RES 4,L',
    0XA6: 'RES 4,(HL)',
    0XA7: 'RES 4,A',
    0XA8: 'RES 5,B',
    0XA9: 'RES 5,C',
    0XAA: 'RES 5,D',
    0XAB: 'RES 5,E',
    0XAC: 'RES 5,H',
    0XAD: 'RES 5,L',
    0XAE: 'RES 5,(HL)',
    0XAF: 'RES 5,A',

    0XB0: 'RES 6,B',
    0XB1: 'RES 6,C',
    0XB2: 'RES 6,D',
    0XB3: 'RES 6,E',
    0XB4: 'RES 6,H',
    0XB5: 'RES 6,L',
    0XB6: 'RES 6,(HL)',
    0XB7: 'RES 6,A',
    0XB8: 'RES 7,B',
    0XB9: 'RES 7,C',
    0XBA: 'RES 7,D',
    0XBB: 'RES 7,E',
    0XBC: 'RES 7,H',
    0XBD: 'RES 7,L',
    0XBE: 'RES 7,(HL)',
    0XBF: 'RES 7,A',


    0XC0: 'SET 0,B',
    0XC1: 'SET 0,C',
    0XC2: 'SET 0,D',
    0XC3: 'SET 0,E',
    0XC4: 'SET 0,H',
    0XC5: 'SET 0,L',
    0XC6: 'SET 0,(HL)',
    0XC7: 'SET 0,A',
    0XC8: 'SET 1,B',
    0XC9: 'SET 1,C',
    0XCA: 'SET 1,D',
    0XCB: 'SET 1,E',
    0XCC: 'SET 1,H',
    0XCD: 'SET 1,L',
    0XCE: 'SET 1,(HL)',
    0XCF: 'SET 1,A',
    
    0XD0: 'SET 2,B',
    0XD1: 'SET 2,C',
    0XD2: 'SET 2,D',
    0XD3: 'SET 2,E',
    0XD4: 'SET 2,H',
    0XD5: 'SET 2,L',
    0XD6: 'SET 2,(HL)',
    0XD7: 'SET 2,A',
    0XD8: 'SET 3,B',
    0XD9: 'SET 3,C',
    0XDA: 'SET 3,D',
    0XDB: 'SET 3,E',
    0XDC: 'SET 3,H',
    0XDD: 'SET 3,L',
    0XDE: 'SET 3,(HL)',
    0XDF: 'SET 3,A',
    
    0XE0: 'SET 4,B',
    0XE1: 'SET 4,C',
    0XE2: 'SET 4,D',
    0XE3: 'SET 4,E',
    0XE4: 'SET 4,H',
    0XE5: 'SET 4,L',
    0XE6: 'SET 4,(HL)',
    0XE7: 'SET 4,A',
    0XE8: 'SET 5,B',
    0XE9: 'SET 5,C',
    0XEA: 'SET 5,D',
    0XEB: 'SET 5,E',
    0XEC: 'SET 5,H',
    0XED: 'SET 5,L',
    0XEE: 'SET 5,(HL)',
    0XEF: 'SET 5,A',

    0XF0: 'SET 6,B',
    0XF1: 'SET 6,C',
    0XF2: 'SET 6,D',
    0XF3: 'SET 6,E',
    0XF4: 'SET 6,H',
    0XF5: 'SET 6,L',
    0XF6: 'SET 6,(HL)',
    0XF7: 'SET 6,A',
    0XF8: 'SET 7,B',
    0XF9: 'SET 7,C',
    0XFA: 'SET 7,D',
    0XFB: 'SET 7,E',
    0XFC: 'SET 7,H',
    0XFD: 'SET 7,L',
    0XFE: 'SET 7,(HL)',
    0XFF: 'SET 7,A'
}

instruction_variants = {
    'hli': {
        'hl+': {
            0X22: 'LD (HL+),A',
            0X2A: 'LD A,(HL+)',
            0X32: 'LD (HL-),A',
            0X3A: 'LD A,(HL-)'
        },
        'hli': {
            0X22: 'LD (HLI),A',
            0X2A: 'LD A,(HLI)',
            0X32: 'LD (HLD),A',
            0X3A: 'LD A,(HLD)'
        },
        'ldi': {
            0X22: 'LDI (HL),A',
            0X2A: 'LDI A,(HL)',
            0X32: 'LDD (HL),A',
            0X3A: 'LDD A,(HL)'
        }
    },
    'ldh_a8': {      
        'ldh_a8': {
            0XE0: 'LDH (A8),A',
            0XF0: 'LDH A,(A8)'
        },
        'ldh_ffa8': {
            0XE0: 'LDH ($FFA8),A',
            0XF0: 'LDH A,($FFA8)'
        },
        'ld_ff00_a8': {
            0XE0: 'LD ($0xff00+A8),A',
            0XF0: 'LD A,($0xff00+A8)'
        },
        'ldh_gb_emu': {
            0XE0: 'LD ($0xff00+A8),A',
            0XF0: 'LD A,($0xff00+A8)'
        },
    },
    'ld_c': {      
        'ld_c': {
            0XE2: 'LD (C),A',
            0XF2: 'LD A,(C)'
        },
        'ldh_c': {
            0XE2: 'LDH (C),A',
            0XF2: 'LDH A,(C)'
        },
        'ld_ff00_c': {
            0XE2: 'LD ($0xff00+C),A',
            0XF2: 'LD A,($0xff00+C)'
        }
    }
}
