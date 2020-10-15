//1811137
grammar BKIT;

@lexer::header {
from lexererr import *
}

@lexer::members {
def emit(self):
    tk = self.type
    result = super().emit()
    if tk == self.UNCLOSE_STRING:       
        raise UncloseString(result.text)
    elif tk == self.ILLEGAL_ESCAPE:
        raise IllegalEscape(result.text)
    elif tk == self.ERROR_CHAR:
        raise ErrorToken(result.text)
    elif tk == self.UNTERMINATED_COMMENT:
        raise UnterminatedComment()
    else:
        return result;
}

options{
	language=Python3;
}

//program  : VAR COLON ID SEMI EOF ;
//program: BOOLEAN;

//ID: [a-z]+ ;

ASSIGN: '=' ;

WS : [ \t\r\n]+ -> skip ; // skip spaces, tabs, newlines


ERROR_CHAR: .;
UNCLOSE_STRING: .;
ILLEGAL_ESCAPE: .;
UNTERMINATED_COMMENT: .;

//PROGRAM COMMENT
COMMENT: '**' .*? '**' -> skip;  // how about appearing in string ?      ** * * **

//TOKENS SET

//Identifiers
ID: [a-z][a-zA-Z_0-9]+;
//Keywords
BODY: 'Body';
BREAK: 'Break';
CONTINUE: 'Continue';
DO: 'Do';
ELSE: 'Else';
ELSEIF: 'ElseIf';
ENDBODY: 'Endbody';
ENDIF: 'EndIf';
ENDFOR: 'Endfor';
ENDWHILE: 'EndWhile';
FOR: 'For';
FUNCTION: 'Function';
IF: 'If';
PARAMETER: 'Parameter';
RETURN: 'Return';
THEN: 'Then';
VAR: 'Var';
WHILE: 'While';
//TRUE: 'True';     //overlap with BOOLEAN
//FALSE: 'False';
ENDDO: 'EndDo';
//Operators
INTADD: '+';
FLOATADD: '+.';
INTSUB: '-';
FLOATSUB: '-.';
INTMUL: '*';
FLOATMUL: '*.';
INTDIV: '\\';
FLOATDIV: '\\.';
INTREMAINDER: '%';
NEG: '!';
CONJUNC: '&&';
DISJUNC: '||';
INTEQUAL: '==';
INTNOTEQUAL: '!=';
INTLESS: '<';
INTGREATER: '>';
INTLESSEQUAL: '<=';
INTGREATEREQUAL: '>=';
FLNOTEQUAL: '=/=';
FLLESS: '<.';
FLGREATER: '>.';
FLLESSEQUAL: '<=.';
FLGREATEREQUAL: '>=.';
//Separator
LB: '(';
RB: ')';
LSB: '[';   //left square bracket
RSB: ']';
COLON: ':' ;
DOT: '.';
COMMA: ',' ;
SEMI: ';' ;
LCB: '{' ; //left curly bracket
RCB: '}' ;
//Literals
INTLIT: '0'+| [1-9][0-9]* //Otherwise, the literal is 0 ????    // 00000 ?
        | ('0x''0X')[1-9A-F][0-9A-F]*
        | ('0o''0O')[1-7][0-7]*;

fragment EXPONENTPART: [Ee][+-]?[0-9]+;
fragment INTPART: ('0'+| [1-9][0-9]*);
fragment DECIMALPART: '.'[0-9]*;
FLOATLIT: INTPART (DECIMALPART| EXPONENTPART| DECIMALPART EXPONENTPART);

//escape sequence is a sequence of characters that they can be in a string if they have a \ before it.
//STRING: '\"' (('\"'|'\b'|'\f'|'\r'|'\n'|'\t'|'\''|'\\')*|~('\''))? '\"';
fragment ESCAPESEQUECE: '\\b'|'\\f'|'\\r'|'\\n'|'\\t'|'\\\''|'\\\\';
STRING_LIT: '"' ( ESCAPESEQUECE* ('\'"' ~('"'|'\\')* '\'"')* ~('"'|'\\')* )* '"'
        {
            y = str(self.text)
            self.text = y[1:-1]
        };

LITERAL: INTLIT | FLOATLIT | STRING | ARRAY;

/*
ARRAYINT: LB INTLIT RB      //how about having multi dimension ?
        | LB INTLIT (COMMA INTLIT)+ RB;
ARRAYFLOAT: LB FLOATLIT RB
        | LB FLOATLIT (COMMA FLOATLIT)+ RB;
ARRAYBOOLEN: LB BOOLEAN RB
        | LB BOOLEAN (COMMA BOOLEAN)+ RB;
ARRAYSTRING: LB STRING RB
        | LB STRING (COMMA STRING)+ RB;
ARRAY: ARRAYINT | ARRAYFLOAT | ARRAYBOOLEN | ARRAYSTRING;
*/
ARRAY: LCB LITERAL RCB    //how about having multi dimension
        | LCB LITERAL (COMMA INTLIT)+ RCB;
//Generate testcase: khai bao 1 array ma trong do co nhieu kieu => error

//TYPE AND VALUE

//boolean
BOOLEAN: 'True'|'False';


program: (vari_declare* fun_declare_list*)*;    //thu tu cua 2 thanh phan

vari_declare: VAR':' variable_list SEMI ;
variable_list: variable COMMA variable_list | variable ;

variable: ID
        | ID ASSIGN LITERAL
        | assign_stm
        | array_vari_declare;
//array_vari_declare: ID LRB

// co nhat thiet ham main phai nam o cuoi cung` ?
fun_declare_list: fun_declare fun_declare_list | fun_declare;
fun_declare: FUNCTION COLON ID fun_para_struct? fun_body; //sau function name, khoang trang ghi chu thi` ?
fun_para_struct: PARAMETER COLON fun_para_list;
fun_para_list: ID COMMA fun_para_list | ID;//chua co truong hop para la 1 array_vari

fun_body: BODY COLON vari_declare* statement_list? ENDBODY DOT;

statement_list: statement statement_list | statement;

statement: assign_stm
        | if_stm
        | for_stm
        | while_stm
        | do_while_stm
        | break_stm
        | continue_stm
        | call_stm
        | return_stm;
assign_stm: ID ASSIGN expression SEMI;       // thieu kieu array
if_stm: IF expression THEN statement_list?   //chua giai quyet expression ko phai la boolean
        (ELSEIF expression THEN statement_list?)*
        (ELSE statement_list?)?
        ENDIF DOT;
for_stm: FOR LB assgin_stm COMMA conditionExpr COMMA updateExpr RB //chua giai quyet assign chi dc la integer
        DO statement_list?
        ENDFOR DOT;
while_stm: WHILE expression DO statement_list? ENDWHILE DOT;//chua giai quyet expression ko phai la boolean
do_while_stm: DO statement_list? WHILE expression ENDDO DOT;//chua giai quyet expression ko phai la boolean
break_stm: BREAK SEMI;//is it a stm ?
continue_stm: CONTINUE SEMI;// is it a stm ?
call_stm: ID LB call_stm_para_list? RB SEMI;
    call_stm_para_list: expression COMMA call_stm_para_list | expression;// co dung ko ?
return_stm: RETURN expression? SEMI// co truong hop RETURN function ko ?
           | RETURN call_stm SEMI;

expression: unary | binary; //bao gom co ID va ko co ID
