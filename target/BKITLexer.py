# Generated from main/bkit/parser/BKIT.g4 by ANTLR 4.8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


from lexererr import *



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2B")
        buf.write("\u0206\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\t")
        buf.write("C\4D\tD\4E\tE\4F\tF\4G\tG\3\2\3\2\3\3\6\3\u0093\n\3\r")
        buf.write("\3\16\3\u0094\3\3\3\3\3\4\3\4\3\4\3\4\7\4\u009d\n\4\f")
        buf.write("\4\16\4\u00a0\13\4\3\4\3\4\3\4\3\4\3\4\3\5\3\5\7\5\u00a9")
        buf.write("\n\5\f\5\16\5\u00ac\13\5\3\6\3\6\3\6\3\6\3\6\3\7\3\7\3")
        buf.write("\7\3\7\3\7\3\7\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\t")
        buf.write("\3\t\3\t\3\n\3\n\3\n\3\n\3\n\3\13\3\13\3\13\3\13\3\13")
        buf.write("\3\13\3\13\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\r\3\r\3\r")
        buf.write("\3\r\3\r\3\r\3\16\3\16\3\16\3\16\3\16\3\16\3\16\3\17\3")
        buf.write("\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\20\3\20\3\20")
        buf.write("\3\20\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\22")
        buf.write("\3\22\3\22\3\23\3\23\3\23\3\23\3\23\3\23\3\23\3\23\3\23")
        buf.write("\3\23\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\25\3\25\3\25")
        buf.write("\3\25\3\25\3\26\3\26\3\26\3\26\3\27\3\27\3\27\3\27\3\27")
        buf.write("\3\27\3\30\3\30\3\30\3\30\3\30\3\30\3\31\3\31\3\32\3\32")
        buf.write("\3\32\3\33\3\33\3\34\3\34\3\34\3\35\3\35\3\36\3\36\3\36")
        buf.write("\3\37\3\37\3 \3 \3 \3!\3!\3\"\3\"\3#\3#\3#\3$\3$\3$\3")
        buf.write("%\3%\3%\3&\3&\3&\3\'\3\'\3(\3(\3)\3)\3)\3*\3*\3*\3+\3")
        buf.write("+\3+\3+\3,\3,\3,\3-\3-\3-\3.\3.\3.\3.\3/\3/\3/\3/\3\60")
        buf.write("\3\60\3\61\3\61\3\62\3\62\3\63\3\63\3\64\3\64\3\65\3\65")
        buf.write("\3\66\3\66\3\67\3\67\38\38\39\39\3:\3:\3:\7:\u017c\n:")
        buf.write("\f:\16:\u017f\13:\3:\3:\3:\3:\5:\u0185\n:\3:\3:\7:\u0189")
        buf.write("\n:\f:\16:\u018c\13:\3:\3:\3:\3:\5:\u0192\n:\3:\3:\7:")
        buf.write("\u0196\n:\f:\16:\u0199\13:\5:\u019b\n:\3;\3;\5;\u019f")
        buf.write("\n;\3;\6;\u01a2\n;\r;\16;\u01a3\3<\6<\u01a7\n<\r<\16<")
        buf.write("\u01a8\3<\6<\u01ac\n<\r<\16<\u01ad\5<\u01b0\n<\3=\3=\7")
        buf.write("=\u01b4\n=\f=\16=\u01b7\13=\3>\3>\3>\3>\3>\3>\5>\u01bf")
        buf.write("\n>\3?\3?\3?\3?\3?\3?\3?\3?\3?\5?\u01ca\n?\3@\3@\3@\3")
        buf.write("A\3A\3A\3A\5A\u01d3\nA\3B\3B\7B\u01d7\nB\fB\16B\u01da")
        buf.write("\13B\3B\3B\3B\3C\3C\3C\3C\5C\u01e3\nC\3D\3D\7D\u01e7\n")
        buf.write("D\fD\16D\u01ea\13D\3D\5D\u01ed\nD\3D\3D\3E\3E\7E\u01f3")
        buf.write("\nE\fE\16E\u01f6\13E\3E\3E\3E\3F\3F\3F\3F\7F\u01ff\nF")
        buf.write("\fF\16F\u0202\13F\3G\3G\3G\4\u009e\u0200\2H\3\3\5\4\7")
        buf.write("\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r\31\16\33\17")
        buf.write("\35\20\37\21!\22#\23%\24\'\25)\26+\27-\30/\31\61\32\63")
        buf.write("\33\65\34\67\359\36;\37= ?!A\"C#E$G%I&K\'M(O)Q*S+U,W-")
        buf.write("Y.[/]\60_\61a\62c\63e\64g\65i\66k\67m8o9q:s;u\2w\2y\2")
        buf.write("{<}=\177\2\u0081\2\u0083>\u0085\2\u0087?\u0089@\u008b")
        buf.write("A\u008dB\3\2\22\5\2\13\f\16\17\"\"\3\2c|\6\2\62;C\\aa")
        buf.write("c|\3\2\63;\3\2\62;\4\2\63;CH\4\2\62;CH\3\2\639\3\2\62")
        buf.write("9\4\2GGgg\4\2--//\t\2))^^ddhhppttvv\6\2\f\f$$))^^\n\2")
        buf.write("$$))^^ddhhppttvv\3\2$$\6\3\n\f\16\17))^^\2\u021a\2\3\3")
        buf.write("\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2")
        buf.write("\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2")
        buf.write("\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2")
        buf.write("\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2")
        buf.write("\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2\2/\3")
        buf.write("\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67\3\2")
        buf.write("\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2A\3")
        buf.write("\2\2\2\2C\3\2\2\2\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2\2K")
        buf.write("\3\2\2\2\2M\3\2\2\2\2O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2\2\2")
        buf.write("U\3\2\2\2\2W\3\2\2\2\2Y\3\2\2\2\2[\3\2\2\2\2]\3\2\2\2")
        buf.write("\2_\3\2\2\2\2a\3\2\2\2\2c\3\2\2\2\2e\3\2\2\2\2g\3\2\2")
        buf.write("\2\2i\3\2\2\2\2k\3\2\2\2\2m\3\2\2\2\2o\3\2\2\2\2q\3\2")
        buf.write("\2\2\2s\3\2\2\2\2{\3\2\2\2\2}\3\2\2\2\2\u0083\3\2\2\2")
        buf.write("\2\u0087\3\2\2\2\2\u0089\3\2\2\2\2\u008b\3\2\2\2\2\u008d")
        buf.write("\3\2\2\2\3\u008f\3\2\2\2\5\u0092\3\2\2\2\7\u0098\3\2\2")
        buf.write("\2\t\u00a6\3\2\2\2\13\u00ad\3\2\2\2\r\u00b2\3\2\2\2\17")
        buf.write("\u00b8\3\2\2\2\21\u00c1\3\2\2\2\23\u00c4\3\2\2\2\25\u00c9")
        buf.write("\3\2\2\2\27\u00d0\3\2\2\2\31\u00d8\3\2\2\2\33\u00de\3")
        buf.write("\2\2\2\35\u00e5\3\2\2\2\37\u00ee\3\2\2\2!\u00f2\3\2\2")
        buf.write("\2#\u00fb\3\2\2\2%\u00fe\3\2\2\2\'\u0108\3\2\2\2)\u010f")
        buf.write("\3\2\2\2+\u0114\3\2\2\2-\u0118\3\2\2\2/\u011e\3\2\2\2")
        buf.write("\61\u0124\3\2\2\2\63\u0126\3\2\2\2\65\u0129\3\2\2\2\67")
        buf.write("\u012b\3\2\2\29\u012e\3\2\2\2;\u0130\3\2\2\2=\u0133\3")
        buf.write("\2\2\2?\u0135\3\2\2\2A\u0138\3\2\2\2C\u013a\3\2\2\2E\u013c")
        buf.write("\3\2\2\2G\u013f\3\2\2\2I\u0142\3\2\2\2K\u0145\3\2\2\2")
        buf.write("M\u0148\3\2\2\2O\u014a\3\2\2\2Q\u014c\3\2\2\2S\u014f\3")
        buf.write("\2\2\2U\u0152\3\2\2\2W\u0156\3\2\2\2Y\u0159\3\2\2\2[\u015c")
        buf.write("\3\2\2\2]\u0160\3\2\2\2_\u0164\3\2\2\2a\u0166\3\2\2\2")
        buf.write("c\u0168\3\2\2\2e\u016a\3\2\2\2g\u016c\3\2\2\2i\u016e\3")
        buf.write("\2\2\2k\u0170\3\2\2\2m\u0172\3\2\2\2o\u0174\3\2\2\2q\u0176")
        buf.write("\3\2\2\2s\u019a\3\2\2\2u\u019c\3\2\2\2w\u01af\3\2\2\2")
        buf.write("y\u01b1\3\2\2\2{\u01b8\3\2\2\2}\u01c9\3\2\2\2\177\u01cb")
        buf.write("\3\2\2\2\u0081\u01d2\3\2\2\2\u0083\u01d4\3\2\2\2\u0085")
        buf.write("\u01e2\3\2\2\2\u0087\u01e4\3\2\2\2\u0089\u01f0\3\2\2\2")
        buf.write("\u008b\u01fa\3\2\2\2\u008d\u0203\3\2\2\2\u008f\u0090\7")
        buf.write("?\2\2\u0090\4\3\2\2\2\u0091\u0093\t\2\2\2\u0092\u0091")
        buf.write("\3\2\2\2\u0093\u0094\3\2\2\2\u0094\u0092\3\2\2\2\u0094")
        buf.write("\u0095\3\2\2\2\u0095\u0096\3\2\2\2\u0096\u0097\b\3\2\2")
        buf.write("\u0097\6\3\2\2\2\u0098\u0099\7,\2\2\u0099\u009a\7,\2\2")
        buf.write("\u009a\u009e\3\2\2\2\u009b\u009d\13\2\2\2\u009c\u009b")
        buf.write("\3\2\2\2\u009d\u00a0\3\2\2\2\u009e\u009f\3\2\2\2\u009e")
        buf.write("\u009c\3\2\2\2\u009f\u00a1\3\2\2\2\u00a0\u009e\3\2\2\2")
        buf.write("\u00a1\u00a2\7,\2\2\u00a2\u00a3\7,\2\2\u00a3\u00a4\3\2")
        buf.write("\2\2\u00a4\u00a5\b\4\2\2\u00a5\b\3\2\2\2\u00a6\u00aa\t")
        buf.write("\3\2\2\u00a7\u00a9\t\4\2\2\u00a8\u00a7\3\2\2\2\u00a9\u00ac")
        buf.write("\3\2\2\2\u00aa\u00a8\3\2\2\2\u00aa\u00ab\3\2\2\2\u00ab")
        buf.write("\n\3\2\2\2\u00ac\u00aa\3\2\2\2\u00ad\u00ae\7D\2\2\u00ae")
        buf.write("\u00af\7q\2\2\u00af\u00b0\7f\2\2\u00b0\u00b1\7{\2\2\u00b1")
        buf.write("\f\3\2\2\2\u00b2\u00b3\7D\2\2\u00b3\u00b4\7t\2\2\u00b4")
        buf.write("\u00b5\7g\2\2\u00b5\u00b6\7c\2\2\u00b6\u00b7\7m\2\2\u00b7")
        buf.write("\16\3\2\2\2\u00b8\u00b9\7E\2\2\u00b9\u00ba\7q\2\2\u00ba")
        buf.write("\u00bb\7p\2\2\u00bb\u00bc\7v\2\2\u00bc\u00bd\7k\2\2\u00bd")
        buf.write("\u00be\7p\2\2\u00be\u00bf\7w\2\2\u00bf\u00c0\7g\2\2\u00c0")
        buf.write("\20\3\2\2\2\u00c1\u00c2\7F\2\2\u00c2\u00c3\7q\2\2\u00c3")
        buf.write("\22\3\2\2\2\u00c4\u00c5\7G\2\2\u00c5\u00c6\7n\2\2\u00c6")
        buf.write("\u00c7\7u\2\2\u00c7\u00c8\7g\2\2\u00c8\24\3\2\2\2\u00c9")
        buf.write("\u00ca\7G\2\2\u00ca\u00cb\7n\2\2\u00cb\u00cc\7u\2\2\u00cc")
        buf.write("\u00cd\7g\2\2\u00cd\u00ce\7K\2\2\u00ce\u00cf\7h\2\2\u00cf")
        buf.write("\26\3\2\2\2\u00d0\u00d1\7G\2\2\u00d1\u00d2\7p\2\2\u00d2")
        buf.write("\u00d3\7f\2\2\u00d3\u00d4\7D\2\2\u00d4\u00d5\7q\2\2\u00d5")
        buf.write("\u00d6\7f\2\2\u00d6\u00d7\7{\2\2\u00d7\30\3\2\2\2\u00d8")
        buf.write("\u00d9\7G\2\2\u00d9\u00da\7p\2\2\u00da\u00db\7f\2\2\u00db")
        buf.write("\u00dc\7K\2\2\u00dc\u00dd\7h\2\2\u00dd\32\3\2\2\2\u00de")
        buf.write("\u00df\7G\2\2\u00df\u00e0\7p\2\2\u00e0\u00e1\7f\2\2\u00e1")
        buf.write("\u00e2\7H\2\2\u00e2\u00e3\7q\2\2\u00e3\u00e4\7t\2\2\u00e4")
        buf.write("\34\3\2\2\2\u00e5\u00e6\7G\2\2\u00e6\u00e7\7p\2\2\u00e7")
        buf.write("\u00e8\7f\2\2\u00e8\u00e9\7Y\2\2\u00e9\u00ea\7j\2\2\u00ea")
        buf.write("\u00eb\7k\2\2\u00eb\u00ec\7n\2\2\u00ec\u00ed\7g\2\2\u00ed")
        buf.write("\36\3\2\2\2\u00ee\u00ef\7H\2\2\u00ef\u00f0\7q\2\2\u00f0")
        buf.write("\u00f1\7t\2\2\u00f1 \3\2\2\2\u00f2\u00f3\7H\2\2\u00f3")
        buf.write("\u00f4\7w\2\2\u00f4\u00f5\7p\2\2\u00f5\u00f6\7e\2\2\u00f6")
        buf.write("\u00f7\7v\2\2\u00f7\u00f8\7k\2\2\u00f8\u00f9\7q\2\2\u00f9")
        buf.write("\u00fa\7p\2\2\u00fa\"\3\2\2\2\u00fb\u00fc\7K\2\2\u00fc")
        buf.write("\u00fd\7h\2\2\u00fd$\3\2\2\2\u00fe\u00ff\7R\2\2\u00ff")
        buf.write("\u0100\7c\2\2\u0100\u0101\7t\2\2\u0101\u0102\7c\2\2\u0102")
        buf.write("\u0103\7o\2\2\u0103\u0104\7g\2\2\u0104\u0105\7v\2\2\u0105")
        buf.write("\u0106\7g\2\2\u0106\u0107\7t\2\2\u0107&\3\2\2\2\u0108")
        buf.write("\u0109\7T\2\2\u0109\u010a\7g\2\2\u010a\u010b\7v\2\2\u010b")
        buf.write("\u010c\7w\2\2\u010c\u010d\7t\2\2\u010d\u010e\7p\2\2\u010e")
        buf.write("(\3\2\2\2\u010f\u0110\7V\2\2\u0110\u0111\7j\2\2\u0111")
        buf.write("\u0112\7g\2\2\u0112\u0113\7p\2\2\u0113*\3\2\2\2\u0114")
        buf.write("\u0115\7X\2\2\u0115\u0116\7c\2\2\u0116\u0117\7t\2\2\u0117")
        buf.write(",\3\2\2\2\u0118\u0119\7Y\2\2\u0119\u011a\7j\2\2\u011a")
        buf.write("\u011b\7k\2\2\u011b\u011c\7n\2\2\u011c\u011d\7g\2\2\u011d")
        buf.write(".\3\2\2\2\u011e\u011f\7G\2\2\u011f\u0120\7p\2\2\u0120")
        buf.write("\u0121\7f\2\2\u0121\u0122\7F\2\2\u0122\u0123\7q\2\2\u0123")
        buf.write("\60\3\2\2\2\u0124\u0125\7-\2\2\u0125\62\3\2\2\2\u0126")
        buf.write("\u0127\7-\2\2\u0127\u0128\7\60\2\2\u0128\64\3\2\2\2\u0129")
        buf.write("\u012a\7/\2\2\u012a\66\3\2\2\2\u012b\u012c\7/\2\2\u012c")
        buf.write("\u012d\7\60\2\2\u012d8\3\2\2\2\u012e\u012f\7,\2\2\u012f")
        buf.write(":\3\2\2\2\u0130\u0131\7,\2\2\u0131\u0132\7\60\2\2\u0132")
        buf.write("<\3\2\2\2\u0133\u0134\7^\2\2\u0134>\3\2\2\2\u0135\u0136")
        buf.write("\7^\2\2\u0136\u0137\7\60\2\2\u0137@\3\2\2\2\u0138\u0139")
        buf.write("\7\'\2\2\u0139B\3\2\2\2\u013a\u013b\7#\2\2\u013bD\3\2")
        buf.write("\2\2\u013c\u013d\7(\2\2\u013d\u013e\7(\2\2\u013eF\3\2")
        buf.write("\2\2\u013f\u0140\7~\2\2\u0140\u0141\7~\2\2\u0141H\3\2")
        buf.write("\2\2\u0142\u0143\7?\2\2\u0143\u0144\7?\2\2\u0144J\3\2")
        buf.write("\2\2\u0145\u0146\7#\2\2\u0146\u0147\7?\2\2\u0147L\3\2")
        buf.write("\2\2\u0148\u0149\7>\2\2\u0149N\3\2\2\2\u014a\u014b\7@")
        buf.write("\2\2\u014bP\3\2\2\2\u014c\u014d\7>\2\2\u014d\u014e\7?")
        buf.write("\2\2\u014eR\3\2\2\2\u014f\u0150\7@\2\2\u0150\u0151\7?")
        buf.write("\2\2\u0151T\3\2\2\2\u0152\u0153\7?\2\2\u0153\u0154\7\61")
        buf.write("\2\2\u0154\u0155\7?\2\2\u0155V\3\2\2\2\u0156\u0157\7>")
        buf.write("\2\2\u0157\u0158\7\60\2\2\u0158X\3\2\2\2\u0159\u015a\7")
        buf.write("@\2\2\u015a\u015b\7\60\2\2\u015bZ\3\2\2\2\u015c\u015d")
        buf.write("\7>\2\2\u015d\u015e\7?\2\2\u015e\u015f\7\60\2\2\u015f")
        buf.write("\\\3\2\2\2\u0160\u0161\7@\2\2\u0161\u0162\7?\2\2\u0162")
        buf.write("\u0163\7\60\2\2\u0163^\3\2\2\2\u0164\u0165\7*\2\2\u0165")
        buf.write("`\3\2\2\2\u0166\u0167\7+\2\2\u0167b\3\2\2\2\u0168\u0169")
        buf.write("\7]\2\2\u0169d\3\2\2\2\u016a\u016b\7_\2\2\u016bf\3\2\2")
        buf.write("\2\u016c\u016d\7<\2\2\u016dh\3\2\2\2\u016e\u016f\7\60")
        buf.write("\2\2\u016fj\3\2\2\2\u0170\u0171\7.\2\2\u0171l\3\2\2\2")
        buf.write("\u0172\u0173\7=\2\2\u0173n\3\2\2\2\u0174\u0175\7}\2\2")
        buf.write("\u0175p\3\2\2\2\u0176\u0177\7\177\2\2\u0177r\3\2\2\2\u0178")
        buf.write("\u019b\7\62\2\2\u0179\u017d\t\5\2\2\u017a\u017c\t\6\2")
        buf.write("\2\u017b\u017a\3\2\2\2\u017c\u017f\3\2\2\2\u017d\u017b")
        buf.write("\3\2\2\2\u017d\u017e\3\2\2\2\u017e\u019b\3\2\2\2\u017f")
        buf.write("\u017d\3\2\2\2\u0180\u0181\7\62\2\2\u0181\u0185\7z\2\2")
        buf.write("\u0182\u0183\7\62\2\2\u0183\u0185\7Z\2\2\u0184\u0180\3")
        buf.write("\2\2\2\u0184\u0182\3\2\2\2\u0185\u0186\3\2\2\2\u0186\u018a")
        buf.write("\t\7\2\2\u0187\u0189\t\b\2\2\u0188\u0187\3\2\2\2\u0189")
        buf.write("\u018c\3\2\2\2\u018a\u0188\3\2\2\2\u018a\u018b\3\2\2\2")
        buf.write("\u018b\u019b\3\2\2\2\u018c\u018a\3\2\2\2\u018d\u018e\7")
        buf.write("\62\2\2\u018e\u0192\7q\2\2\u018f\u0190\7\62\2\2\u0190")
        buf.write("\u0192\7Q\2\2\u0191\u018d\3\2\2\2\u0191\u018f\3\2\2\2")
        buf.write("\u0192\u0193\3\2\2\2\u0193\u0197\t\t\2\2\u0194\u0196\t")
        buf.write("\n\2\2\u0195\u0194\3\2\2\2\u0196\u0199\3\2\2\2\u0197\u0195")
        buf.write("\3\2\2\2\u0197\u0198\3\2\2\2\u0198\u019b\3\2\2\2\u0199")
        buf.write("\u0197\3\2\2\2\u019a\u0178\3\2\2\2\u019a\u0179\3\2\2\2")
        buf.write("\u019a\u0184\3\2\2\2\u019a\u0191\3\2\2\2\u019bt\3\2\2")
        buf.write("\2\u019c\u019e\t\13\2\2\u019d\u019f\t\f\2\2\u019e\u019d")
        buf.write("\3\2\2\2\u019e\u019f\3\2\2\2\u019f\u01a1\3\2\2\2\u01a0")
        buf.write("\u01a2\t\6\2\2\u01a1\u01a0\3\2\2\2\u01a2\u01a3\3\2\2\2")
        buf.write("\u01a3\u01a1\3\2\2\2\u01a3\u01a4\3\2\2\2\u01a4v\3\2\2")
        buf.write("\2\u01a5\u01a7\7\62\2\2\u01a6\u01a5\3\2\2\2\u01a7\u01a8")
        buf.write("\3\2\2\2\u01a8\u01a6\3\2\2\2\u01a8\u01a9\3\2\2\2\u01a9")
        buf.write("\u01b0\3\2\2\2\u01aa\u01ac\t\6\2\2\u01ab\u01aa\3\2\2\2")
        buf.write("\u01ac\u01ad\3\2\2\2\u01ad\u01ab\3\2\2\2\u01ad\u01ae\3")
        buf.write("\2\2\2\u01ae\u01b0\3\2\2\2\u01af\u01a6\3\2\2\2\u01af\u01ab")
        buf.write("\3\2\2\2\u01b0x\3\2\2\2\u01b1\u01b5\7\60\2\2\u01b2\u01b4")
        buf.write("\t\6\2\2\u01b3\u01b2\3\2\2\2\u01b4\u01b7\3\2\2\2\u01b5")
        buf.write("\u01b3\3\2\2\2\u01b5\u01b6\3\2\2\2\u01b6z\3\2\2\2\u01b7")
        buf.write("\u01b5\3\2\2\2\u01b8\u01be\5w<\2\u01b9\u01bf\5y=\2\u01ba")
        buf.write("\u01bf\5u;\2\u01bb\u01bc\5y=\2\u01bc\u01bd\5u;\2\u01bd")
        buf.write("\u01bf\3\2\2\2\u01be\u01b9\3\2\2\2\u01be\u01ba\3\2\2\2")
        buf.write("\u01be\u01bb\3\2\2\2\u01bf|\3\2\2\2\u01c0\u01c1\7V\2\2")
        buf.write("\u01c1\u01c2\7t\2\2\u01c2\u01c3\7w\2\2\u01c3\u01ca\7g")
        buf.write("\2\2\u01c4\u01c5\7H\2\2\u01c5\u01c6\7c\2\2\u01c6\u01c7")
        buf.write("\7n\2\2\u01c7\u01c8\7u\2\2\u01c8\u01ca\7g\2\2\u01c9\u01c0")
        buf.write("\3\2\2\2\u01c9\u01c4\3\2\2\2\u01ca~\3\2\2\2\u01cb\u01cc")
        buf.write("\7^\2\2\u01cc\u01cd\t\r\2\2\u01cd\u0080\3\2\2\2\u01ce")
        buf.write("\u01d3\5\177@\2\u01cf\u01d3\n\16\2\2\u01d0\u01d1\7)\2")
        buf.write("\2\u01d1\u01d3\7$\2\2\u01d2\u01ce\3\2\2\2\u01d2\u01cf")
        buf.write("\3\2\2\2\u01d2\u01d0\3\2\2\2\u01d3\u0082\3\2\2\2\u01d4")
        buf.write("\u01d8\7$\2\2\u01d5\u01d7\5\u0081A\2\u01d6\u01d5\3\2\2")
        buf.write("\2\u01d7\u01da\3\2\2\2\u01d8\u01d6\3\2\2\2\u01d8\u01d9")
        buf.write("\3\2\2\2\u01d9\u01db\3\2\2\2\u01da\u01d8\3\2\2\2\u01db")
        buf.write("\u01dc\7$\2\2\u01dc\u01dd\bB\3\2\u01dd\u0084\3\2\2\2\u01de")
        buf.write("\u01df\7^\2\2\u01df\u01e3\n\17\2\2\u01e0\u01e1\7)\2\2")
        buf.write("\u01e1\u01e3\n\20\2\2\u01e2\u01de\3\2\2\2\u01e2\u01e0")
        buf.write("\3\2\2\2\u01e3\u0086\3\2\2\2\u01e4\u01e8\7$\2\2\u01e5")
        buf.write("\u01e7\5\u0081A\2\u01e6\u01e5\3\2\2\2\u01e7\u01ea\3\2")
        buf.write("\2\2\u01e8\u01e6\3\2\2\2\u01e8\u01e9\3\2\2\2\u01e9\u01ec")
        buf.write("\3\2\2\2\u01ea\u01e8\3\2\2\2\u01eb\u01ed\t\21\2\2\u01ec")
        buf.write("\u01eb\3\2\2\2\u01ed\u01ee\3\2\2\2\u01ee\u01ef\bD\4\2")
        buf.write("\u01ef\u0088\3\2\2\2\u01f0\u01f4\7$\2\2\u01f1\u01f3\5")
        buf.write("\u0081A\2\u01f2\u01f1\3\2\2\2\u01f3\u01f6\3\2\2\2\u01f4")
        buf.write("\u01f2\3\2\2\2\u01f4\u01f5\3\2\2\2\u01f5\u01f7\3\2\2\2")
        buf.write("\u01f6\u01f4\3\2\2\2\u01f7\u01f8\5\u0085C\2\u01f8\u01f9")
        buf.write("\bE\5\2\u01f9\u008a\3\2\2\2\u01fa\u01fb\7,\2\2\u01fb\u01fc")
        buf.write("\7,\2\2\u01fc\u0200\3\2\2\2\u01fd\u01ff\13\2\2\2\u01fe")
        buf.write("\u01fd\3\2\2\2\u01ff\u0202\3\2\2\2\u0200\u0201\3\2\2\2")
        buf.write("\u0200\u01fe\3\2\2\2\u0201\u008c\3\2\2\2\u0202\u0200\3")
        buf.write("\2\2\2\u0203\u0204\13\2\2\2\u0204\u0205\bG\6\2\u0205\u008e")
        buf.write("\3\2\2\2\33\2\u0094\u009e\u00aa\u017d\u0184\u018a\u0191")
        buf.write("\u0197\u019a\u019e\u01a3\u01a8\u01ad\u01af\u01b5\u01be")
        buf.write("\u01c9\u01d2\u01d8\u01e2\u01e8\u01ec\u01f4\u0200\7\b\2")
        buf.write("\2\3B\2\3D\3\3E\4\3G\5")
        return buf.getvalue()


class BKITLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    ASSIGN = 1
    WS = 2
    COMMENT = 3
    ID = 4
    BODY = 5
    BREAK = 6
    CONTINUE = 7
    DO = 8
    ELSE = 9
    ELSEIF = 10
    ENDBODY = 11
    ENDIF = 12
    ENDFOR = 13
    ENDWHILE = 14
    FOR = 15
    FUNCTION = 16
    IF = 17
    PARAMETER = 18
    RETURN = 19
    THEN = 20
    VAR = 21
    WHILE = 22
    ENDDO = 23
    INTADD = 24
    FLOATADD = 25
    INTSUB = 26
    FLOATSUB = 27
    INTMUL = 28
    FLOATMUL = 29
    INTDIV = 30
    FLOATDIV = 31
    INTREMAINDER = 32
    NEG = 33
    CONJUNC = 34
    DISJUNC = 35
    INTEQUAL = 36
    INTNOTEQUAL = 37
    INTLESS = 38
    INTGREATER = 39
    INTLESSEQUAL = 40
    INTGREATEREQUAL = 41
    FLNOTEQUAL = 42
    FLLESS = 43
    FLGREATER = 44
    FLLESSEQUAL = 45
    FLGREATEREQUAL = 46
    LB = 47
    RB = 48
    LSB = 49
    RSB = 50
    COLON = 51
    DOT = 52
    COMMA = 53
    SEMI = 54
    LCB = 55
    RCB = 56
    INTLIT = 57
    FLOATLIT = 58
    BOOLEANLIT = 59
    STRING_LIT = 60
    UNCLOSE_STRING = 61
    ILLEGAL_ESCAPE = 62
    UNTERMINATED_COMMENT = 63
    ERROR_CHAR = 64

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'='", "'Body'", "'Break'", "'Continue'", "'Do'", "'Else'", 
            "'ElseIf'", "'EndBody'", "'EndIf'", "'EndFor'", "'EndWhile'", 
            "'For'", "'Function'", "'If'", "'Parameter'", "'Return'", "'Then'", 
            "'Var'", "'While'", "'EndDo'", "'+'", "'+.'", "'-'", "'-.'", 
            "'*'", "'*.'", "'\\'", "'\\.'", "'%'", "'!'", "'&&'", "'||'", 
            "'=='", "'!='", "'<'", "'>'", "'<='", "'>='", "'=/='", "'<.'", 
            "'>.'", "'<=.'", "'>=.'", "'('", "')'", "'['", "']'", "':'", 
            "'.'", "','", "';'", "'{'", "'}'" ]

    symbolicNames = [ "<INVALID>",
            "ASSIGN", "WS", "COMMENT", "ID", "BODY", "BREAK", "CONTINUE", 
            "DO", "ELSE", "ELSEIF", "ENDBODY", "ENDIF", "ENDFOR", "ENDWHILE", 
            "FOR", "FUNCTION", "IF", "PARAMETER", "RETURN", "THEN", "VAR", 
            "WHILE", "ENDDO", "INTADD", "FLOATADD", "INTSUB", "FLOATSUB", 
            "INTMUL", "FLOATMUL", "INTDIV", "FLOATDIV", "INTREMAINDER", 
            "NEG", "CONJUNC", "DISJUNC", "INTEQUAL", "INTNOTEQUAL", "INTLESS", 
            "INTGREATER", "INTLESSEQUAL", "INTGREATEREQUAL", "FLNOTEQUAL", 
            "FLLESS", "FLGREATER", "FLLESSEQUAL", "FLGREATEREQUAL", "LB", 
            "RB", "LSB", "RSB", "COLON", "DOT", "COMMA", "SEMI", "LCB", 
            "RCB", "INTLIT", "FLOATLIT", "BOOLEANLIT", "STRING_LIT", "UNCLOSE_STRING", 
            "ILLEGAL_ESCAPE", "UNTERMINATED_COMMENT", "ERROR_CHAR" ]

    ruleNames = [ "ASSIGN", "WS", "COMMENT", "ID", "BODY", "BREAK", "CONTINUE", 
                  "DO", "ELSE", "ELSEIF", "ENDBODY", "ENDIF", "ENDFOR", 
                  "ENDWHILE", "FOR", "FUNCTION", "IF", "PARAMETER", "RETURN", 
                  "THEN", "VAR", "WHILE", "ENDDO", "INTADD", "FLOATADD", 
                  "INTSUB", "FLOATSUB", "INTMUL", "FLOATMUL", "INTDIV", 
                  "FLOATDIV", "INTREMAINDER", "NEG", "CONJUNC", "DISJUNC", 
                  "INTEQUAL", "INTNOTEQUAL", "INTLESS", "INTGREATER", "INTLESSEQUAL", 
                  "INTGREATEREQUAL", "FLNOTEQUAL", "FLLESS", "FLGREATER", 
                  "FLLESSEQUAL", "FLGREATEREQUAL", "LB", "RB", "LSB", "RSB", 
                  "COLON", "DOT", "COMMA", "SEMI", "LCB", "RCB", "INTLIT", 
                  "EXPONENTPART", "INTPART", "DECIMALPART", "FLOATLIT", 
                  "BOOLEANLIT", "ESCAPESEQUECE", "STR_CHARACTER", "STRING_LIT", 
                  "ESC_ILLEGAL", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", "UNTERMINATED_COMMENT", 
                  "ERROR_CHAR" ]

    grammarFileName = "BKIT.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.8")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


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


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
        if self._actions is None:
            actions = dict()
            actions[64] = self.STRING_LIT_action 
            actions[66] = self.UNCLOSE_STRING_action 
            actions[67] = self.ILLEGAL_ESCAPE_action 
            actions[69] = self.ERROR_CHAR_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def STRING_LIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:

                        a = str(self.text)
                        self.text = a[1:-1]
                    
     

    def UNCLOSE_STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 1:

            		a = str(self.text)
            		possible = ['\b', '\t', '\n', '\f', '\r',  "'", '\\']
            		if a[-1] in possible:
            			raise UncloseString(a[1:-1])
            		else:
            			raise UncloseString(a[1:])
            	
     

    def ILLEGAL_ESCAPE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 2:

            		a = str(self.text)
            		raise IllegalEscape(a[1:])
            	
     

    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 3:

            		raise ErrorToken(self.text)
            	
     


