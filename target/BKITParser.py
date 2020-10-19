# Generated from main/bkit/parser/BKIT.g4 by ANTLR 4.8
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3B")
        buf.write("\u01b4\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\3\2\3\2")
        buf.write("\6\2]\n\2\r\2\16\2^\3\2\3\2\3\3\3\3\3\3\3\3\3\3\3\4\3")
        buf.write("\4\3\4\3\4\3\4\5\4m\n\4\3\5\3\5\3\5\5\5r\n\5\3\5\3\5\3")
        buf.write("\5\3\5\5\5x\n\5\3\6\3\6\3\6\3\6\3\6\7\6\177\n\6\f\6\16")
        buf.write("\6\u0082\13\6\3\7\3\7\3\7\3\7\3\b\3\b\3\b\3\b\3\b\5\b")
        buf.write("\u008d\n\b\3\t\3\t\5\t\u0091\n\t\3\n\3\n\3\n\3\n\5\n\u0097")
        buf.write("\n\n\3\n\3\n\3\13\3\13\3\13\3\13\3\f\3\f\3\f\3\f\3\f\5")
        buf.write("\f\u00a4\n\f\3\r\3\r\3\r\5\r\u00a9\n\r\3\r\3\r\3\r\3\16")
        buf.write("\7\16\u00af\n\16\f\16\16\16\u00b2\13\16\3\16\3\16\3\17")
        buf.write("\3\17\3\17\3\17\5\17\u00ba\n\17\3\20\3\20\3\20\3\20\3")
        buf.write("\20\3\21\3\21\3\21\3\21\3\21\5\21\u00c6\n\21\3\22\3\22")
        buf.write("\3\22\3\22\3\22\3\22\3\22\5\22\u00cf\n\22\5\22\u00d1\n")
        buf.write("\22\3\23\3\23\3\23\3\23\3\23\3\23\3\23\3\23\3\23\5\23")
        buf.write("\u00dc\n\23\3\24\3\24\3\24\3\24\3\24\3\25\3\25\3\25\3")
        buf.write("\25\5\25\u00e7\n\25\3\25\3\25\3\25\3\25\5\25\u00ed\n\25")
        buf.write("\7\25\u00ef\n\25\f\25\16\25\u00f2\13\25\3\25\3\25\5\25")
        buf.write("\u00f6\n\25\5\25\u00f8\n\25\3\25\3\25\3\25\3\26\3\26\3")
        buf.write("\26\3\26\3\26\3\26\3\26\3\26\3\26\3\26\3\26\3\26\5\26")
        buf.write("\u0109\n\26\3\26\3\26\3\26\3\27\3\27\3\27\3\27\5\27\u0112")
        buf.write("\n\27\3\27\3\27\3\27\3\30\3\30\5\30\u0119\n\30\3\30\3")
        buf.write("\30\3\30\3\30\3\30\3\31\3\31\3\31\3\32\3\32\3\32\3\33")
        buf.write("\3\33\3\33\5\33\u0129\n\33\3\33\3\33\3\33\3\34\3\34\3")
        buf.write("\34\3\34\3\34\5\34\u0133\n\34\3\35\3\35\5\35\u0137\n\35")
        buf.write("\3\35\3\35\3\36\3\36\3\36\3\36\3\36\3\36\3\36\3\36\3\36")
        buf.write("\3\36\3\36\3\36\5\36\u0147\n\36\3\37\3\37\3 \3 \3!\3!")
        buf.write("\3\"\3\"\3\"\3\"\3\"\5\"\u0154\n\"\3#\3#\3#\3#\3#\3#\3")
        buf.write("#\7#\u015d\n#\f#\16#\u0160\13#\3$\3$\3$\3$\3$\3$\3$\7")
        buf.write("$\u0169\n$\f$\16$\u016c\13$\3%\3%\3%\3%\3%\3%\3%\7%\u0175")
        buf.write("\n%\f%\16%\u0178\13%\3&\3&\3&\5&\u017d\n&\3\'\3\'\3\'")
        buf.write("\5\'\u0182\n\'\3(\3(\3(\3(\3(\7(\u0189\n(\f(\16(\u018c")
        buf.write("\13(\3)\3)\3)\3)\3)\3)\3)\3)\3)\5)\u0197\n)\3*\3*\3*\3")
        buf.write("*\3*\3*\3*\5*\u01a0\n*\3+\3+\3+\3+\3+\5+\u01a7\n+\3+\3")
        buf.write("+\5+\u01ab\n+\3,\5,\u01ae\n,\3,\3,\3-\3-\3-\2\6DFHN.\2")
        buf.write("\4\6\b\n\f\16\20\22\24\26\30\32\34\36 \"$&(*,.\60\62\64")
        buf.write("\668:<>@BDFHJLNPRTVX\2\7\3\2$%\3\2\32\35\3\2\36\"\3\2")
        buf.write("\34\35\3\2;>\2\u01c3\2\\\3\2\2\2\4b\3\2\2\2\6l\3\2\2\2")
        buf.write("\bw\3\2\2\2\ny\3\2\2\2\f\u0083\3\2\2\2\16\u008c\3\2\2")
        buf.write("\2\20\u0090\3\2\2\2\22\u0092\3\2\2\2\24\u009a\3\2\2\2")
        buf.write("\26\u00a3\3\2\2\2\30\u00a5\3\2\2\2\32\u00b0\3\2\2\2\34")
        buf.write("\u00b9\3\2\2\2\36\u00bb\3\2\2\2 \u00c5\3\2\2\2\"\u00d0")
        buf.write("\3\2\2\2$\u00db\3\2\2\2&\u00dd\3\2\2\2(\u00e2\3\2\2\2")
        buf.write("*\u00fc\3\2\2\2,\u010d\3\2\2\2.\u0116\3\2\2\2\60\u011f")
        buf.write("\3\2\2\2\62\u0122\3\2\2\2\64\u0125\3\2\2\2\66\u0132\3")
        buf.write("\2\2\28\u0134\3\2\2\2:\u0146\3\2\2\2<\u0148\3\2\2\2>\u014a")
        buf.write("\3\2\2\2@\u014c\3\2\2\2B\u0153\3\2\2\2D\u0155\3\2\2\2")
        buf.write("F\u0161\3\2\2\2H\u016d\3\2\2\2J\u017c\3\2\2\2L\u0181\3")
        buf.write("\2\2\2N\u0183\3\2\2\2P\u0196\3\2\2\2R\u019f\3\2\2\2T\u01aa")
        buf.write("\3\2\2\2V\u01ad\3\2\2\2X\u01b1\3\2\2\2Z]\5\4\3\2[]\5\22")
        buf.write("\n\2\\Z\3\2\2\2\\[\3\2\2\2]^\3\2\2\2^\\\3\2\2\2^_\3\2")
        buf.write("\2\2_`\3\2\2\2`a\7\2\2\3a\3\3\2\2\2bc\7\27\2\2cd\7\65")
        buf.write("\2\2de\5\6\4\2ef\78\2\2f\5\3\2\2\2gh\5\b\5\2hi\7\67\2")
        buf.write("\2ij\5\6\4\2jm\3\2\2\2km\5\b\5\2lg\3\2\2\2lk\3\2\2\2m")
        buf.write("\7\3\2\2\2nq\5\n\6\2op\7\3\2\2pr\5X-\2qo\3\2\2\2qr\3\2")
        buf.write("\2\2rx\3\2\2\2st\5\n\6\2tu\7\3\2\2uv\5\f\7\2vx\3\2\2\2")
        buf.write("wn\3\2\2\2ws\3\2\2\2x\t\3\2\2\2y\u0080\7\6\2\2z{\7\63")
        buf.write("\2\2{|\5B\"\2|}\7\64\2\2}\177\3\2\2\2~z\3\2\2\2\177\u0082")
        buf.write("\3\2\2\2\u0080~\3\2\2\2\u0080\u0081\3\2\2\2\u0081\13\3")
        buf.write("\2\2\2\u0082\u0080\3\2\2\2\u0083\u0084\79\2\2\u0084\u0085")
        buf.write("\5\16\b\2\u0085\u0086\7:\2\2\u0086\r\3\2\2\2\u0087\u0088")
        buf.write("\5\20\t\2\u0088\u0089\7\67\2\2\u0089\u008a\5\16\b\2\u008a")
        buf.write("\u008d\3\2\2\2\u008b\u008d\5\20\t\2\u008c\u0087\3\2\2")
        buf.write("\2\u008c\u008b\3\2\2\2\u008d\17\3\2\2\2\u008e\u0091\5")
        buf.write("\f\7\2\u008f\u0091\5X-\2\u0090\u008e\3\2\2\2\u0090\u008f")
        buf.write("\3\2\2\2\u0091\21\3\2\2\2\u0092\u0093\7\22\2\2\u0093\u0094")
        buf.write("\7\65\2\2\u0094\u0096\7\6\2\2\u0095\u0097\5\24\13\2\u0096")
        buf.write("\u0095\3\2\2\2\u0096\u0097\3\2\2\2\u0097\u0098\3\2\2\2")
        buf.write("\u0098\u0099\5\30\r\2\u0099\23\3\2\2\2\u009a\u009b\7\24")
        buf.write("\2\2\u009b\u009c\7\65\2\2\u009c\u009d\5\26\f\2\u009d\25")
        buf.write("\3\2\2\2\u009e\u009f\5\n\6\2\u009f\u00a0\7\67\2\2\u00a0")
        buf.write("\u00a1\5\26\f\2\u00a1\u00a4\3\2\2\2\u00a2\u00a4\5\n\6")
        buf.write("\2\u00a3\u009e\3\2\2\2\u00a3\u00a2\3\2\2\2\u00a4\27\3")
        buf.write("\2\2\2\u00a5\u00a6\7\7\2\2\u00a6\u00a8\7\65\2\2\u00a7")
        buf.write("\u00a9\5\32\16\2\u00a8\u00a7\3\2\2\2\u00a8\u00a9\3\2\2")
        buf.write("\2\u00a9\u00aa\3\2\2\2\u00aa\u00ab\7\r\2\2\u00ab\u00ac")
        buf.write("\7\66\2\2\u00ac\31\3\2\2\2\u00ad\u00af\5\36\20\2\u00ae")
        buf.write("\u00ad\3\2\2\2\u00af\u00b2\3\2\2\2\u00b0\u00ae\3\2\2\2")
        buf.write("\u00b0\u00b1\3\2\2\2\u00b1\u00b3\3\2\2\2\u00b2\u00b0\3")
        buf.write("\2\2\2\u00b3\u00b4\5\34\17\2\u00b4\33\3\2\2\2\u00b5\u00b6")
        buf.write("\5$\23\2\u00b6\u00b7\5\34\17\2\u00b7\u00ba\3\2\2\2\u00b8")
        buf.write("\u00ba\5$\23\2\u00b9\u00b5\3\2\2\2\u00b9\u00b8\3\2\2\2")
        buf.write("\u00ba\35\3\2\2\2\u00bb\u00bc\7\27\2\2\u00bc\u00bd\7\65")
        buf.write("\2\2\u00bd\u00be\5 \21\2\u00be\u00bf\78\2\2\u00bf\37\3")
        buf.write("\2\2\2\u00c0\u00c1\5\"\22\2\u00c1\u00c2\7\67\2\2\u00c2")
        buf.write("\u00c3\5 \21\2\u00c3\u00c6\3\2\2\2\u00c4\u00c6\5\"\22")
        buf.write("\2\u00c5\u00c0\3\2\2\2\u00c5\u00c4\3\2\2\2\u00c6!\3\2")
        buf.write("\2\2\u00c7\u00c8\5\n\6\2\u00c8\u00c9\7\3\2\2\u00c9\u00ca")
        buf.write("\5\f\7\2\u00ca\u00d1\3\2\2\2\u00cb\u00ce\5\n\6\2\u00cc")
        buf.write("\u00cd\7\3\2\2\u00cd\u00cf\5B\"\2\u00ce\u00cc\3\2\2\2")
        buf.write("\u00ce\u00cf\3\2\2\2\u00cf\u00d1\3\2\2\2\u00d0\u00c7\3")
        buf.write("\2\2\2\u00d0\u00cb\3\2\2\2\u00d1#\3\2\2\2\u00d2\u00dc")
        buf.write("\5&\24\2\u00d3\u00dc\5(\25\2\u00d4\u00dc\5*\26\2\u00d5")
        buf.write("\u00dc\5,\27\2\u00d6\u00dc\5.\30\2\u00d7\u00dc\5\60\31")
        buf.write("\2\u00d8\u00dc\5\62\32\2\u00d9\u00dc\5\64\33\2\u00da\u00dc")
        buf.write("\58\35\2\u00db\u00d2\3\2\2\2\u00db\u00d3\3\2\2\2\u00db")
        buf.write("\u00d4\3\2\2\2\u00db\u00d5\3\2\2\2\u00db\u00d6\3\2\2\2")
        buf.write("\u00db\u00d7\3\2\2\2\u00db\u00d8\3\2\2\2\u00db\u00d9\3")
        buf.write("\2\2\2\u00db\u00da\3\2\2\2\u00dc%\3\2\2\2\u00dd\u00de")
        buf.write("\5\n\6\2\u00de\u00df\7\3\2\2\u00df\u00e0\5B\"\2\u00e0")
        buf.write("\u00e1\78\2\2\u00e1\'\3\2\2\2\u00e2\u00e3\7\23\2\2\u00e3")
        buf.write("\u00e4\5B\"\2\u00e4\u00e6\7\26\2\2\u00e5\u00e7\5\32\16")
        buf.write("\2\u00e6\u00e5\3\2\2\2\u00e6\u00e7\3\2\2\2\u00e7\u00f0")
        buf.write("\3\2\2\2\u00e8\u00e9\7\f\2\2\u00e9\u00ea\5B\"\2\u00ea")
        buf.write("\u00ec\7\26\2\2\u00eb\u00ed\5\32\16\2\u00ec\u00eb\3\2")
        buf.write("\2\2\u00ec\u00ed\3\2\2\2\u00ed\u00ef\3\2\2\2\u00ee\u00e8")
        buf.write("\3\2\2\2\u00ef\u00f2\3\2\2\2\u00f0\u00ee\3\2\2\2\u00f0")
        buf.write("\u00f1\3\2\2\2\u00f1\u00f7\3\2\2\2\u00f2\u00f0\3\2\2\2")
        buf.write("\u00f3\u00f5\7\13\2\2\u00f4\u00f6\5\32\16\2\u00f5\u00f4")
        buf.write("\3\2\2\2\u00f5\u00f6\3\2\2\2\u00f6\u00f8\3\2\2\2\u00f7")
        buf.write("\u00f3\3\2\2\2\u00f7\u00f8\3\2\2\2\u00f8\u00f9\3\2\2\2")
        buf.write("\u00f9\u00fa\7\16\2\2\u00fa\u00fb\7\66\2\2\u00fb)\3\2")
        buf.write("\2\2\u00fc\u00fd\7\21\2\2\u00fd\u00fe\7\61\2\2\u00fe\u00ff")
        buf.write("\7\6\2\2\u00ff\u0100\7\3\2\2\u0100\u0101\5B\"\2\u0101")
        buf.write("\u0102\7\67\2\2\u0102\u0103\5B\"\2\u0103\u0104\7\67\2")
        buf.write("\2\u0104\u0105\5B\"\2\u0105\u0106\7\62\2\2\u0106\u0108")
        buf.write("\7\n\2\2\u0107\u0109\5\32\16\2\u0108\u0107\3\2\2\2\u0108")
        buf.write("\u0109\3\2\2\2\u0109\u010a\3\2\2\2\u010a\u010b\7\17\2")
        buf.write("\2\u010b\u010c\7\66\2\2\u010c+\3\2\2\2\u010d\u010e\7\30")
        buf.write("\2\2\u010e\u010f\5B\"\2\u010f\u0111\7\n\2\2\u0110\u0112")
        buf.write("\5\32\16\2\u0111\u0110\3\2\2\2\u0111\u0112\3\2\2\2\u0112")
        buf.write("\u0113\3\2\2\2\u0113\u0114\7\20\2\2\u0114\u0115\7\66\2")
        buf.write("\2\u0115-\3\2\2\2\u0116\u0118\7\n\2\2\u0117\u0119\5\32")
        buf.write("\16\2\u0118\u0117\3\2\2\2\u0118\u0119\3\2\2\2\u0119\u011a")
        buf.write("\3\2\2\2\u011a\u011b\7\30\2\2\u011b\u011c\5B\"\2\u011c")
        buf.write("\u011d\7\31\2\2\u011d\u011e\7\66\2\2\u011e/\3\2\2\2\u011f")
        buf.write("\u0120\7\b\2\2\u0120\u0121\78\2\2\u0121\61\3\2\2\2\u0122")
        buf.write("\u0123\7\t\2\2\u0123\u0124\78\2\2\u0124\63\3\2\2\2\u0125")
        buf.write("\u0126\7\6\2\2\u0126\u0128\7\61\2\2\u0127\u0129\5\66\34")
        buf.write("\2\u0128\u0127\3\2\2\2\u0128\u0129\3\2\2\2\u0129\u012a")
        buf.write("\3\2\2\2\u012a\u012b\7\62\2\2\u012b\u012c\78\2\2\u012c")
        buf.write("\65\3\2\2\2\u012d\u012e\5B\"\2\u012e\u012f\7\67\2\2\u012f")
        buf.write("\u0130\5\66\34\2\u0130\u0133\3\2\2\2\u0131\u0133\5B\"")
        buf.write("\2\u0132\u012d\3\2\2\2\u0132\u0131\3\2\2\2\u0133\67\3")
        buf.write("\2\2\2\u0134\u0136\7\25\2\2\u0135\u0137\5B\"\2\u0136\u0135")
        buf.write("\3\2\2\2\u0136\u0137\3\2\2\2\u0137\u0138\3\2\2\2\u0138")
        buf.write("\u0139\78\2\2\u01399\3\2\2\2\u013a\u0147\3\2\2\2\u013b")
        buf.write("\u0147\7&\2\2\u013c\u0147\7\'\2\2\u013d\u0147\7(\2\2\u013e")
        buf.write("\u0147\7)\2\2\u013f\u0147\7*\2\2\u0140\u0147\7+\2\2\u0141")
        buf.write("\u0147\7,\2\2\u0142\u0147\7-\2\2\u0143\u0147\7.\2\2\u0144")
        buf.write("\u0147\7/\2\2\u0145\u0147\7\60\2\2\u0146\u013a\3\2\2\2")
        buf.write("\u0146\u013b\3\2\2\2\u0146\u013c\3\2\2\2\u0146\u013d\3")
        buf.write("\2\2\2\u0146\u013e\3\2\2\2\u0146\u013f\3\2\2\2\u0146\u0140")
        buf.write("\3\2\2\2\u0146\u0141\3\2\2\2\u0146\u0142\3\2\2\2\u0146")
        buf.write("\u0143\3\2\2\2\u0146\u0144\3\2\2\2\u0146\u0145\3\2\2\2")
        buf.write("\u0147;\3\2\2\2\u0148\u0149\t\2\2\2\u0149=\3\2\2\2\u014a")
        buf.write("\u014b\t\3\2\2\u014b?\3\2\2\2\u014c\u014d\t\4\2\2\u014d")
        buf.write("A\3\2\2\2\u014e\u014f\5D#\2\u014f\u0150\5:\36\2\u0150")
        buf.write("\u0151\5D#\2\u0151\u0154\3\2\2\2\u0152\u0154\5D#\2\u0153")
        buf.write("\u014e\3\2\2\2\u0153\u0152\3\2\2\2\u0154C\3\2\2\2\u0155")
        buf.write("\u0156\b#\1\2\u0156\u0157\5F$\2\u0157\u015e\3\2\2\2\u0158")
        buf.write("\u0159\f\4\2\2\u0159\u015a\5<\37\2\u015a\u015b\5F$\2\u015b")
        buf.write("\u015d\3\2\2\2\u015c\u0158\3\2\2\2\u015d\u0160\3\2\2\2")
        buf.write("\u015e\u015c\3\2\2\2\u015e\u015f\3\2\2\2\u015fE\3\2\2")
        buf.write("\2\u0160\u015e\3\2\2\2\u0161\u0162\b$\1\2\u0162\u0163")
        buf.write("\5H%\2\u0163\u016a\3\2\2\2\u0164\u0165\f\4\2\2\u0165\u0166")
        buf.write("\5> \2\u0166\u0167\5H%\2\u0167\u0169\3\2\2\2\u0168\u0164")
        buf.write("\3\2\2\2\u0169\u016c\3\2\2\2\u016a\u0168\3\2\2\2\u016a")
        buf.write("\u016b\3\2\2\2\u016bG\3\2\2\2\u016c\u016a\3\2\2\2\u016d")
        buf.write("\u016e\b%\1\2\u016e\u016f\5J&\2\u016f\u0176\3\2\2\2\u0170")
        buf.write("\u0171\f\4\2\2\u0171\u0172\5@!\2\u0172\u0173\5J&\2\u0173")
        buf.write("\u0175\3\2\2\2\u0174\u0170\3\2\2\2\u0175\u0178\3\2\2\2")
        buf.write("\u0176\u0174\3\2\2\2\u0176\u0177\3\2\2\2\u0177I\3\2\2")
        buf.write("\2\u0178\u0176\3\2\2\2\u0179\u017a\7#\2\2\u017a\u017d")
        buf.write("\5J&\2\u017b\u017d\5L\'\2\u017c\u0179\3\2\2\2\u017c\u017b")
        buf.write("\3\2\2\2\u017dK\3\2\2\2\u017e\u017f\t\5\2\2\u017f\u0182")
        buf.write("\5L\'\2\u0180\u0182\5N(\2\u0181\u017e\3\2\2\2\u0181\u0180")
        buf.write("\3\2\2\2\u0182M\3\2\2\2\u0183\u0184\b(\1\2\u0184\u0185")
        buf.write("\5R*\2\u0185\u018a\3\2\2\2\u0186\u0187\f\4\2\2\u0187\u0189")
        buf.write("\5P)\2\u0188\u0186\3\2\2\2\u0189\u018c\3\2\2\2\u018a\u0188")
        buf.write("\3\2\2\2\u018a\u018b\3\2\2\2\u018bO\3\2\2\2\u018c\u018a")
        buf.write("\3\2\2\2\u018d\u018e\7\63\2\2\u018e\u018f\5B\"\2\u018f")
        buf.write("\u0190\7\64\2\2\u0190\u0191\5P)\2\u0191\u0197\3\2\2\2")
        buf.write("\u0192\u0193\7\63\2\2\u0193\u0194\5B\"\2\u0194\u0195\7")
        buf.write("\64\2\2\u0195\u0197\3\2\2\2\u0196\u018d\3\2\2\2\u0196")
        buf.write("\u0192\3\2\2\2\u0197Q\3\2\2\2\u0198\u0199\7\6\2\2\u0199")
        buf.write("\u019a\7\61\2\2\u019a\u019b\5\66\34\2\u019b\u019c\7\62")
        buf.write("\2\2\u019c\u019d\5T+\2\u019d\u01a0\3\2\2\2\u019e\u01a0")
        buf.write("\5T+\2\u019f\u0198\3\2\2\2\u019f\u019e\3\2\2\2\u01a0S")
        buf.write("\3\2\2\2\u01a1\u01ab\5V,\2\u01a2\u01ab\5\n\6\2\u01a3\u01a4")
        buf.write("\7\6\2\2\u01a4\u01a6\7\61\2\2\u01a5\u01a7\5\66\34\2\u01a6")
        buf.write("\u01a5\3\2\2\2\u01a6\u01a7\3\2\2\2\u01a7\u01a8\3\2\2\2")
        buf.write("\u01a8\u01ab\7\62\2\2\u01a9\u01ab\5X-\2\u01aa\u01a1\3")
        buf.write("\2\2\2\u01aa\u01a2\3\2\2\2\u01aa\u01a3\3\2\2\2\u01aa\u01a9")
        buf.write("\3\2\2\2\u01abU\3\2\2\2\u01ac\u01ae\t\5\2\2\u01ad\u01ac")
        buf.write("\3\2\2\2\u01ad\u01ae\3\2\2\2\u01ae\u01af\3\2\2\2\u01af")
        buf.write("\u01b0\5X-\2\u01b0W\3\2\2\2\u01b1\u01b2\t\6\2\2\u01b2")
        buf.write("Y\3\2\2\2+\\^lqw\u0080\u008c\u0090\u0096\u00a3\u00a8\u00b0")
        buf.write("\u00b9\u00c5\u00ce\u00d0\u00db\u00e6\u00ec\u00f0\u00f5")
        buf.write("\u00f7\u0108\u0111\u0118\u0128\u0132\u0136\u0146\u0153")
        buf.write("\u015e\u016a\u0176\u017c\u0181\u018a\u0196\u019f\u01a6")
        buf.write("\u01aa\u01ad")
        return buf.getvalue()


class BKITParser ( Parser ):

    grammarFileName = "BKIT.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'='", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "'Body'", "'Break'", "'Continue'", "'Do'", "'Else'", 
                     "'ElseIf'", "'EndBody'", "'EndIf'", "'EndFor'", "'EndWhile'", 
                     "'For'", "'Function'", "'If'", "'Parameter'", "'Return'", 
                     "'Then'", "'Var'", "'While'", "'EndDo'", "'+'", "'+.'", 
                     "'-'", "'-.'", "'*'", "'*.'", "'\\'", "'\\.'", "'%'", 
                     "'!'", "'&&'", "'||'", "'=='", "'!='", "'<'", "'>'", 
                     "'<='", "'>='", "'=/='", "'<.'", "'>.'", "'<=.'", "'>=.'", 
                     "'('", "')'", "'['", "']'", "':'", "'.'", "','", "';'", 
                     "'{'", "'}'" ]

    symbolicNames = [ "<INVALID>", "ASSIGN", "WS", "COMMENT", "ID", "BODY", 
                      "BREAK", "CONTINUE", "DO", "ELSE", "ELSEIF", "ENDBODY", 
                      "ENDIF", "ENDFOR", "ENDWHILE", "FOR", "FUNCTION", 
                      "IF", "PARAMETER", "RETURN", "THEN", "VAR", "WHILE", 
                      "ENDDO", "INTADD", "FLOATADD", "INTSUB", "FLOATSUB", 
                      "INTMUL", "FLOATMUL", "INTDIV", "FLOATDIV", "INTREMAINDER", 
                      "NEG", "CONJUNC", "DISJUNC", "INTEQUAL", "INTNOTEQUAL", 
                      "INTLESS", "INTGREATER", "INTLESSEQUAL", "INTGREATEREQUAL", 
                      "FLNOTEQUAL", "FLLESS", "FLGREATER", "FLLESSEQUAL", 
                      "FLGREATEREQUAL", "LB", "RB", "LSB", "RSB", "COLON", 
                      "DOT", "COMMA", "SEMI", "LCB", "RCB", "INTLIT", "FLOATLIT", 
                      "BOOLEANLIT", "STRING_LIT", "ERROR_CHAR", "UNCLOSE_STRING", 
                      "ILLEGAL_ESCAPE", "UNTERMINATED_COMMENT" ]

    RULE_program = 0
    RULE_glo_vari_declare = 1
    RULE_glo_variable_list = 2
    RULE_vari_intval = 3
    RULE_variable = 4
    RULE_array = 5
    RULE_list_literal = 6
    RULE_t = 7
    RULE_fun_declare = 8
    RULE_fun_para_struct = 9
    RULE_fun_para_list = 10
    RULE_fun_body = 11
    RULE_statement_list = 12
    RULE_statement_not_declare = 13
    RULE_local_vari_declare = 14
    RULE_local_variable_list = 15
    RULE_vari_intval_id = 16
    RULE_statement = 17
    RULE_assign_stm = 18
    RULE_if_stm = 19
    RULE_for_stm = 20
    RULE_while_stm = 21
    RULE_do_while_stm = 22
    RULE_break_stm = 23
    RULE_continue_stm = 24
    RULE_call_stm = 25
    RULE_call_stm_para_list = 26
    RULE_return_stm = 27
    RULE_relational_op = 28
    RULE_logical_op = 29
    RULE_adding_op = 30
    RULE_multiplying_op = 31
    RULE_exp = 32
    RULE_exp1 = 33
    RULE_exp2 = 34
    RULE_exp3 = 35
    RULE_exp4 = 36
    RULE_exp5 = 37
    RULE_exp6 = 38
    RULE_index_operators = 39
    RULE_exp7 = 40
    RULE_operand = 41
    RULE_constants = 42
    RULE_literal = 43

    ruleNames =  [ "program", "glo_vari_declare", "glo_variable_list", "vari_intval", 
                   "variable", "array", "list_literal", "t", "fun_declare", 
                   "fun_para_struct", "fun_para_list", "fun_body", "statement_list", 
                   "statement_not_declare", "local_vari_declare", "local_variable_list", 
                   "vari_intval_id", "statement", "assign_stm", "if_stm", 
                   "for_stm", "while_stm", "do_while_stm", "break_stm", 
                   "continue_stm", "call_stm", "call_stm_para_list", "return_stm", 
                   "relational_op", "logical_op", "adding_op", "multiplying_op", 
                   "exp", "exp1", "exp2", "exp3", "exp4", "exp5", "exp6", 
                   "index_operators", "exp7", "operand", "constants", "literal" ]

    EOF = Token.EOF
    ASSIGN=1
    WS=2
    COMMENT=3
    ID=4
    BODY=5
    BREAK=6
    CONTINUE=7
    DO=8
    ELSE=9
    ELSEIF=10
    ENDBODY=11
    ENDIF=12
    ENDFOR=13
    ENDWHILE=14
    FOR=15
    FUNCTION=16
    IF=17
    PARAMETER=18
    RETURN=19
    THEN=20
    VAR=21
    WHILE=22
    ENDDO=23
    INTADD=24
    FLOATADD=25
    INTSUB=26
    FLOATSUB=27
    INTMUL=28
    FLOATMUL=29
    INTDIV=30
    FLOATDIV=31
    INTREMAINDER=32
    NEG=33
    CONJUNC=34
    DISJUNC=35
    INTEQUAL=36
    INTNOTEQUAL=37
    INTLESS=38
    INTGREATER=39
    INTLESSEQUAL=40
    INTGREATEREQUAL=41
    FLNOTEQUAL=42
    FLLESS=43
    FLGREATER=44
    FLLESSEQUAL=45
    FLGREATEREQUAL=46
    LB=47
    RB=48
    LSB=49
    RSB=50
    COLON=51
    DOT=52
    COMMA=53
    SEMI=54
    LCB=55
    RCB=56
    INTLIT=57
    FLOATLIT=58
    BOOLEANLIT=59
    STRING_LIT=60
    ERROR_CHAR=61
    UNCLOSE_STRING=62
    ILLEGAL_ESCAPE=63
    UNTERMINATED_COMMENT=64

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.8")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(BKITParser.EOF, 0)

        def glo_vari_declare(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKITParser.Glo_vari_declareContext)
            else:
                return self.getTypedRuleContext(BKITParser.Glo_vari_declareContext,i)


        def fun_declare(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKITParser.Fun_declareContext)
            else:
                return self.getTypedRuleContext(BKITParser.Fun_declareContext,i)


        def getRuleIndex(self):
            return BKITParser.RULE_program

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = BKITParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 90 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 90
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [BKITParser.VAR]:
                    self.state = 88
                    self.glo_vari_declare()
                    pass
                elif token in [BKITParser.FUNCTION]:
                    self.state = 89
                    self.fun_declare()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 92 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==BKITParser.FUNCTION or _la==BKITParser.VAR):
                    break

            self.state = 94
            self.match(BKITParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Glo_vari_declareContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VAR(self):
            return self.getToken(BKITParser.VAR, 0)

        def COLON(self):
            return self.getToken(BKITParser.COLON, 0)

        def glo_variable_list(self):
            return self.getTypedRuleContext(BKITParser.Glo_variable_listContext,0)


        def SEMI(self):
            return self.getToken(BKITParser.SEMI, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_glo_vari_declare

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitGlo_vari_declare" ):
                return visitor.visitGlo_vari_declare(self)
            else:
                return visitor.visitChildren(self)




    def glo_vari_declare(self):

        localctx = BKITParser.Glo_vari_declareContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_glo_vari_declare)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 96
            self.match(BKITParser.VAR)
            self.state = 97
            self.match(BKITParser.COLON)
            self.state = 98
            self.glo_variable_list()
            self.state = 99
            self.match(BKITParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Glo_variable_listContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def vari_intval(self):
            return self.getTypedRuleContext(BKITParser.Vari_intvalContext,0)


        def COMMA(self):
            return self.getToken(BKITParser.COMMA, 0)

        def glo_variable_list(self):
            return self.getTypedRuleContext(BKITParser.Glo_variable_listContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_glo_variable_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitGlo_variable_list" ):
                return visitor.visitGlo_variable_list(self)
            else:
                return visitor.visitChildren(self)




    def glo_variable_list(self):

        localctx = BKITParser.Glo_variable_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_glo_variable_list)
        try:
            self.state = 106
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 101
                self.vari_intval()
                self.state = 102
                self.match(BKITParser.COMMA)
                self.state = 103
                self.glo_variable_list()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 105
                self.vari_intval()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Vari_intvalContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def variable(self):
            return self.getTypedRuleContext(BKITParser.VariableContext,0)


        def ASSIGN(self):
            return self.getToken(BKITParser.ASSIGN, 0)

        def literal(self):
            return self.getTypedRuleContext(BKITParser.LiteralContext,0)


        def array(self):
            return self.getTypedRuleContext(BKITParser.ArrayContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_vari_intval

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVari_intval" ):
                return visitor.visitVari_intval(self)
            else:
                return visitor.visitChildren(self)




    def vari_intval(self):

        localctx = BKITParser.Vari_intvalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_vari_intval)
        self._la = 0 # Token type
        try:
            self.state = 117
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 108
                self.variable()
                self.state = 111
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==BKITParser.ASSIGN:
                    self.state = 109
                    self.match(BKITParser.ASSIGN)
                    self.state = 110
                    self.literal()


                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 113
                self.variable()

                self.state = 114
                self.match(BKITParser.ASSIGN)
                self.state = 115
                self.array()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VariableContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(BKITParser.ID, 0)

        def LSB(self, i:int=None):
            if i is None:
                return self.getTokens(BKITParser.LSB)
            else:
                return self.getToken(BKITParser.LSB, i)

        def exp(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKITParser.ExpContext)
            else:
                return self.getTypedRuleContext(BKITParser.ExpContext,i)


        def RSB(self, i:int=None):
            if i is None:
                return self.getTokens(BKITParser.RSB)
            else:
                return self.getToken(BKITParser.RSB, i)

        def getRuleIndex(self):
            return BKITParser.RULE_variable

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVariable" ):
                return visitor.visitVariable(self)
            else:
                return visitor.visitChildren(self)




    def variable(self):

        localctx = BKITParser.VariableContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_variable)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 119
            self.match(BKITParser.ID)
            self.state = 126
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,5,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 120
                    self.match(BKITParser.LSB)
                    self.state = 121
                    self.exp()
                    self.state = 122
                    self.match(BKITParser.RSB) 
                self.state = 128
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,5,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArrayContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LCB(self):
            return self.getToken(BKITParser.LCB, 0)

        def list_literal(self):
            return self.getTypedRuleContext(BKITParser.List_literalContext,0)


        def RCB(self):
            return self.getToken(BKITParser.RCB, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_array

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray" ):
                return visitor.visitArray(self)
            else:
                return visitor.visitChildren(self)




    def array(self):

        localctx = BKITParser.ArrayContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_array)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 129
            self.match(BKITParser.LCB)
            self.state = 130
            self.list_literal()
            self.state = 131
            self.match(BKITParser.RCB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class List_literalContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def t(self):
            return self.getTypedRuleContext(BKITParser.TContext,0)


        def COMMA(self):
            return self.getToken(BKITParser.COMMA, 0)

        def list_literal(self):
            return self.getTypedRuleContext(BKITParser.List_literalContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_list_literal

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitList_literal" ):
                return visitor.visitList_literal(self)
            else:
                return visitor.visitChildren(self)




    def list_literal(self):

        localctx = BKITParser.List_literalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_list_literal)
        try:
            self.state = 138
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 133
                self.t()
                self.state = 134
                self.match(BKITParser.COMMA)
                self.state = 135
                self.list_literal()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 137
                self.t()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def array(self):
            return self.getTypedRuleContext(BKITParser.ArrayContext,0)


        def literal(self):
            return self.getTypedRuleContext(BKITParser.LiteralContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_t

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitT" ):
                return visitor.visitT(self)
            else:
                return visitor.visitChildren(self)




    def t(self):

        localctx = BKITParser.TContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_t)
        try:
            self.state = 142
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKITParser.LCB]:
                self.enterOuterAlt(localctx, 1)
                self.state = 140
                self.array()
                pass
            elif token in [BKITParser.INTLIT, BKITParser.FLOATLIT, BKITParser.BOOLEANLIT, BKITParser.STRING_LIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 141
                self.literal()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Fun_declareContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FUNCTION(self):
            return self.getToken(BKITParser.FUNCTION, 0)

        def COLON(self):
            return self.getToken(BKITParser.COLON, 0)

        def ID(self):
            return self.getToken(BKITParser.ID, 0)

        def fun_body(self):
            return self.getTypedRuleContext(BKITParser.Fun_bodyContext,0)


        def fun_para_struct(self):
            return self.getTypedRuleContext(BKITParser.Fun_para_structContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_fun_declare

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFun_declare" ):
                return visitor.visitFun_declare(self)
            else:
                return visitor.visitChildren(self)




    def fun_declare(self):

        localctx = BKITParser.Fun_declareContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_fun_declare)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 144
            self.match(BKITParser.FUNCTION)
            self.state = 145
            self.match(BKITParser.COLON)
            self.state = 146
            self.match(BKITParser.ID)
            self.state = 148
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BKITParser.PARAMETER:
                self.state = 147
                self.fun_para_struct()


            self.state = 150
            self.fun_body()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Fun_para_structContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PARAMETER(self):
            return self.getToken(BKITParser.PARAMETER, 0)

        def COLON(self):
            return self.getToken(BKITParser.COLON, 0)

        def fun_para_list(self):
            return self.getTypedRuleContext(BKITParser.Fun_para_listContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_fun_para_struct

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFun_para_struct" ):
                return visitor.visitFun_para_struct(self)
            else:
                return visitor.visitChildren(self)




    def fun_para_struct(self):

        localctx = BKITParser.Fun_para_structContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_fun_para_struct)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 152
            self.match(BKITParser.PARAMETER)
            self.state = 153
            self.match(BKITParser.COLON)
            self.state = 154
            self.fun_para_list()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Fun_para_listContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def variable(self):
            return self.getTypedRuleContext(BKITParser.VariableContext,0)


        def COMMA(self):
            return self.getToken(BKITParser.COMMA, 0)

        def fun_para_list(self):
            return self.getTypedRuleContext(BKITParser.Fun_para_listContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_fun_para_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFun_para_list" ):
                return visitor.visitFun_para_list(self)
            else:
                return visitor.visitChildren(self)




    def fun_para_list(self):

        localctx = BKITParser.Fun_para_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_fun_para_list)
        try:
            self.state = 161
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 156
                self.variable()
                self.state = 157
                self.match(BKITParser.COMMA)
                self.state = 158
                self.fun_para_list()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 160
                self.variable()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Fun_bodyContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BODY(self):
            return self.getToken(BKITParser.BODY, 0)

        def COLON(self):
            return self.getToken(BKITParser.COLON, 0)

        def ENDBODY(self):
            return self.getToken(BKITParser.ENDBODY, 0)

        def DOT(self):
            return self.getToken(BKITParser.DOT, 0)

        def statement_list(self):
            return self.getTypedRuleContext(BKITParser.Statement_listContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_fun_body

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFun_body" ):
                return visitor.visitFun_body(self)
            else:
                return visitor.visitChildren(self)




    def fun_body(self):

        localctx = BKITParser.Fun_bodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_fun_body)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 163
            self.match(BKITParser.BODY)
            self.state = 164
            self.match(BKITParser.COLON)
            self.state = 166
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKITParser.ID) | (1 << BKITParser.BREAK) | (1 << BKITParser.CONTINUE) | (1 << BKITParser.DO) | (1 << BKITParser.FOR) | (1 << BKITParser.IF) | (1 << BKITParser.RETURN) | (1 << BKITParser.VAR) | (1 << BKITParser.WHILE))) != 0):
                self.state = 165
                self.statement_list()


            self.state = 168
            self.match(BKITParser.ENDBODY)
            self.state = 169
            self.match(BKITParser.DOT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Statement_listContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statement_not_declare(self):
            return self.getTypedRuleContext(BKITParser.Statement_not_declareContext,0)


        def local_vari_declare(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKITParser.Local_vari_declareContext)
            else:
                return self.getTypedRuleContext(BKITParser.Local_vari_declareContext,i)


        def getRuleIndex(self):
            return BKITParser.RULE_statement_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement_list" ):
                return visitor.visitStatement_list(self)
            else:
                return visitor.visitChildren(self)




    def statement_list(self):

        localctx = BKITParser.Statement_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_statement_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 174
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BKITParser.VAR:
                self.state = 171
                self.local_vari_declare()
                self.state = 176
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 177
            self.statement_not_declare()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Statement_not_declareContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statement(self):
            return self.getTypedRuleContext(BKITParser.StatementContext,0)


        def statement_not_declare(self):
            return self.getTypedRuleContext(BKITParser.Statement_not_declareContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_statement_not_declare

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement_not_declare" ):
                return visitor.visitStatement_not_declare(self)
            else:
                return visitor.visitChildren(self)




    def statement_not_declare(self):

        localctx = BKITParser.Statement_not_declareContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_statement_not_declare)
        try:
            self.state = 183
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 179
                self.statement()
                self.state = 180
                self.statement_not_declare()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 182
                self.statement()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Local_vari_declareContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VAR(self):
            return self.getToken(BKITParser.VAR, 0)

        def COLON(self):
            return self.getToken(BKITParser.COLON, 0)

        def local_variable_list(self):
            return self.getTypedRuleContext(BKITParser.Local_variable_listContext,0)


        def SEMI(self):
            return self.getToken(BKITParser.SEMI, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_local_vari_declare

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLocal_vari_declare" ):
                return visitor.visitLocal_vari_declare(self)
            else:
                return visitor.visitChildren(self)




    def local_vari_declare(self):

        localctx = BKITParser.Local_vari_declareContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_local_vari_declare)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 185
            self.match(BKITParser.VAR)
            self.state = 186
            self.match(BKITParser.COLON)
            self.state = 187
            self.local_variable_list()
            self.state = 188
            self.match(BKITParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Local_variable_listContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def vari_intval_id(self):
            return self.getTypedRuleContext(BKITParser.Vari_intval_idContext,0)


        def COMMA(self):
            return self.getToken(BKITParser.COMMA, 0)

        def local_variable_list(self):
            return self.getTypedRuleContext(BKITParser.Local_variable_listContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_local_variable_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLocal_variable_list" ):
                return visitor.visitLocal_variable_list(self)
            else:
                return visitor.visitChildren(self)




    def local_variable_list(self):

        localctx = BKITParser.Local_variable_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_local_variable_list)
        try:
            self.state = 195
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 190
                self.vari_intval_id()
                self.state = 191
                self.match(BKITParser.COMMA)
                self.state = 192
                self.local_variable_list()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 194
                self.vari_intval_id()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Vari_intval_idContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def variable(self):
            return self.getTypedRuleContext(BKITParser.VariableContext,0)


        def ASSIGN(self):
            return self.getToken(BKITParser.ASSIGN, 0)

        def array(self):
            return self.getTypedRuleContext(BKITParser.ArrayContext,0)


        def exp(self):
            return self.getTypedRuleContext(BKITParser.ExpContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_vari_intval_id

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVari_intval_id" ):
                return visitor.visitVari_intval_id(self)
            else:
                return visitor.visitChildren(self)




    def vari_intval_id(self):

        localctx = BKITParser.Vari_intval_idContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_vari_intval_id)
        self._la = 0 # Token type
        try:
            self.state = 206
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 197
                self.variable()

                self.state = 198
                self.match(BKITParser.ASSIGN)
                self.state = 199
                self.array()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 201
                self.variable()
                self.state = 204
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==BKITParser.ASSIGN:
                    self.state = 202
                    self.match(BKITParser.ASSIGN)
                    self.state = 203
                    self.exp()


                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def assign_stm(self):
            return self.getTypedRuleContext(BKITParser.Assign_stmContext,0)


        def if_stm(self):
            return self.getTypedRuleContext(BKITParser.If_stmContext,0)


        def for_stm(self):
            return self.getTypedRuleContext(BKITParser.For_stmContext,0)


        def while_stm(self):
            return self.getTypedRuleContext(BKITParser.While_stmContext,0)


        def do_while_stm(self):
            return self.getTypedRuleContext(BKITParser.Do_while_stmContext,0)


        def break_stm(self):
            return self.getTypedRuleContext(BKITParser.Break_stmContext,0)


        def continue_stm(self):
            return self.getTypedRuleContext(BKITParser.Continue_stmContext,0)


        def call_stm(self):
            return self.getTypedRuleContext(BKITParser.Call_stmContext,0)


        def return_stm(self):
            return self.getTypedRuleContext(BKITParser.Return_stmContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement" ):
                return visitor.visitStatement(self)
            else:
                return visitor.visitChildren(self)




    def statement(self):

        localctx = BKITParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_statement)
        try:
            self.state = 217
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,16,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 208
                self.assign_stm()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 209
                self.if_stm()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 210
                self.for_stm()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 211
                self.while_stm()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 212
                self.do_while_stm()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 213
                self.break_stm()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 214
                self.continue_stm()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 215
                self.call_stm()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 216
                self.return_stm()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Assign_stmContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def variable(self):
            return self.getTypedRuleContext(BKITParser.VariableContext,0)


        def ASSIGN(self):
            return self.getToken(BKITParser.ASSIGN, 0)

        def exp(self):
            return self.getTypedRuleContext(BKITParser.ExpContext,0)


        def SEMI(self):
            return self.getToken(BKITParser.SEMI, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_assign_stm

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssign_stm" ):
                return visitor.visitAssign_stm(self)
            else:
                return visitor.visitChildren(self)




    def assign_stm(self):

        localctx = BKITParser.Assign_stmContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_assign_stm)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 219
            self.variable()
            self.state = 220
            self.match(BKITParser.ASSIGN)
            self.state = 221
            self.exp()
            self.state = 222
            self.match(BKITParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class If_stmContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(BKITParser.IF, 0)

        def exp(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKITParser.ExpContext)
            else:
                return self.getTypedRuleContext(BKITParser.ExpContext,i)


        def THEN(self, i:int=None):
            if i is None:
                return self.getTokens(BKITParser.THEN)
            else:
                return self.getToken(BKITParser.THEN, i)

        def ENDIF(self):
            return self.getToken(BKITParser.ENDIF, 0)

        def DOT(self):
            return self.getToken(BKITParser.DOT, 0)

        def statement_list(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKITParser.Statement_listContext)
            else:
                return self.getTypedRuleContext(BKITParser.Statement_listContext,i)


        def ELSEIF(self, i:int=None):
            if i is None:
                return self.getTokens(BKITParser.ELSEIF)
            else:
                return self.getToken(BKITParser.ELSEIF, i)

        def ELSE(self):
            return self.getToken(BKITParser.ELSE, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_if_stm

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIf_stm" ):
                return visitor.visitIf_stm(self)
            else:
                return visitor.visitChildren(self)




    def if_stm(self):

        localctx = BKITParser.If_stmContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_if_stm)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 224
            self.match(BKITParser.IF)
            self.state = 225
            self.exp()
            self.state = 226
            self.match(BKITParser.THEN)
            self.state = 228
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKITParser.ID) | (1 << BKITParser.BREAK) | (1 << BKITParser.CONTINUE) | (1 << BKITParser.DO) | (1 << BKITParser.FOR) | (1 << BKITParser.IF) | (1 << BKITParser.RETURN) | (1 << BKITParser.VAR) | (1 << BKITParser.WHILE))) != 0):
                self.state = 227
                self.statement_list()


            self.state = 238
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BKITParser.ELSEIF:
                self.state = 230
                self.match(BKITParser.ELSEIF)
                self.state = 231
                self.exp()
                self.state = 232
                self.match(BKITParser.THEN)
                self.state = 234
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKITParser.ID) | (1 << BKITParser.BREAK) | (1 << BKITParser.CONTINUE) | (1 << BKITParser.DO) | (1 << BKITParser.FOR) | (1 << BKITParser.IF) | (1 << BKITParser.RETURN) | (1 << BKITParser.VAR) | (1 << BKITParser.WHILE))) != 0):
                    self.state = 233
                    self.statement_list()


                self.state = 240
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 245
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BKITParser.ELSE:
                self.state = 241
                self.match(BKITParser.ELSE)
                self.state = 243
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKITParser.ID) | (1 << BKITParser.BREAK) | (1 << BKITParser.CONTINUE) | (1 << BKITParser.DO) | (1 << BKITParser.FOR) | (1 << BKITParser.IF) | (1 << BKITParser.RETURN) | (1 << BKITParser.VAR) | (1 << BKITParser.WHILE))) != 0):
                    self.state = 242
                    self.statement_list()




            self.state = 247
            self.match(BKITParser.ENDIF)
            self.state = 248
            self.match(BKITParser.DOT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class For_stmContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FOR(self):
            return self.getToken(BKITParser.FOR, 0)

        def LB(self):
            return self.getToken(BKITParser.LB, 0)

        def ID(self):
            return self.getToken(BKITParser.ID, 0)

        def ASSIGN(self):
            return self.getToken(BKITParser.ASSIGN, 0)

        def exp(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKITParser.ExpContext)
            else:
                return self.getTypedRuleContext(BKITParser.ExpContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(BKITParser.COMMA)
            else:
                return self.getToken(BKITParser.COMMA, i)

        def RB(self):
            return self.getToken(BKITParser.RB, 0)

        def DO(self):
            return self.getToken(BKITParser.DO, 0)

        def ENDFOR(self):
            return self.getToken(BKITParser.ENDFOR, 0)

        def DOT(self):
            return self.getToken(BKITParser.DOT, 0)

        def statement_list(self):
            return self.getTypedRuleContext(BKITParser.Statement_listContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_for_stm

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFor_stm" ):
                return visitor.visitFor_stm(self)
            else:
                return visitor.visitChildren(self)




    def for_stm(self):

        localctx = BKITParser.For_stmContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_for_stm)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 250
            self.match(BKITParser.FOR)
            self.state = 251
            self.match(BKITParser.LB)
            self.state = 252
            self.match(BKITParser.ID)
            self.state = 253
            self.match(BKITParser.ASSIGN)
            self.state = 254
            self.exp()
            self.state = 255
            self.match(BKITParser.COMMA)
            self.state = 256
            self.exp()
            self.state = 257
            self.match(BKITParser.COMMA)
            self.state = 258
            self.exp()
            self.state = 259
            self.match(BKITParser.RB)
            self.state = 260
            self.match(BKITParser.DO)
            self.state = 262
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKITParser.ID) | (1 << BKITParser.BREAK) | (1 << BKITParser.CONTINUE) | (1 << BKITParser.DO) | (1 << BKITParser.FOR) | (1 << BKITParser.IF) | (1 << BKITParser.RETURN) | (1 << BKITParser.VAR) | (1 << BKITParser.WHILE))) != 0):
                self.state = 261
                self.statement_list()


            self.state = 264
            self.match(BKITParser.ENDFOR)
            self.state = 265
            self.match(BKITParser.DOT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class While_stmContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WHILE(self):
            return self.getToken(BKITParser.WHILE, 0)

        def exp(self):
            return self.getTypedRuleContext(BKITParser.ExpContext,0)


        def DO(self):
            return self.getToken(BKITParser.DO, 0)

        def ENDWHILE(self):
            return self.getToken(BKITParser.ENDWHILE, 0)

        def DOT(self):
            return self.getToken(BKITParser.DOT, 0)

        def statement_list(self):
            return self.getTypedRuleContext(BKITParser.Statement_listContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_while_stm

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWhile_stm" ):
                return visitor.visitWhile_stm(self)
            else:
                return visitor.visitChildren(self)




    def while_stm(self):

        localctx = BKITParser.While_stmContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_while_stm)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 267
            self.match(BKITParser.WHILE)
            self.state = 268
            self.exp()
            self.state = 269
            self.match(BKITParser.DO)
            self.state = 271
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKITParser.ID) | (1 << BKITParser.BREAK) | (1 << BKITParser.CONTINUE) | (1 << BKITParser.DO) | (1 << BKITParser.FOR) | (1 << BKITParser.IF) | (1 << BKITParser.RETURN) | (1 << BKITParser.VAR) | (1 << BKITParser.WHILE))) != 0):
                self.state = 270
                self.statement_list()


            self.state = 273
            self.match(BKITParser.ENDWHILE)
            self.state = 274
            self.match(BKITParser.DOT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Do_while_stmContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DO(self):
            return self.getToken(BKITParser.DO, 0)

        def WHILE(self):
            return self.getToken(BKITParser.WHILE, 0)

        def exp(self):
            return self.getTypedRuleContext(BKITParser.ExpContext,0)


        def ENDDO(self):
            return self.getToken(BKITParser.ENDDO, 0)

        def DOT(self):
            return self.getToken(BKITParser.DOT, 0)

        def statement_list(self):
            return self.getTypedRuleContext(BKITParser.Statement_listContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_do_while_stm

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDo_while_stm" ):
                return visitor.visitDo_while_stm(self)
            else:
                return visitor.visitChildren(self)




    def do_while_stm(self):

        localctx = BKITParser.Do_while_stmContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_do_while_stm)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 276
            self.match(BKITParser.DO)
            self.state = 278
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,24,self._ctx)
            if la_ == 1:
                self.state = 277
                self.statement_list()


            self.state = 280
            self.match(BKITParser.WHILE)
            self.state = 281
            self.exp()
            self.state = 282
            self.match(BKITParser.ENDDO)
            self.state = 283
            self.match(BKITParser.DOT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Break_stmContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BREAK(self):
            return self.getToken(BKITParser.BREAK, 0)

        def SEMI(self):
            return self.getToken(BKITParser.SEMI, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_break_stm

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBreak_stm" ):
                return visitor.visitBreak_stm(self)
            else:
                return visitor.visitChildren(self)




    def break_stm(self):

        localctx = BKITParser.Break_stmContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_break_stm)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 285
            self.match(BKITParser.BREAK)
            self.state = 286
            self.match(BKITParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Continue_stmContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CONTINUE(self):
            return self.getToken(BKITParser.CONTINUE, 0)

        def SEMI(self):
            return self.getToken(BKITParser.SEMI, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_continue_stm

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitContinue_stm" ):
                return visitor.visitContinue_stm(self)
            else:
                return visitor.visitChildren(self)




    def continue_stm(self):

        localctx = BKITParser.Continue_stmContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_continue_stm)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 288
            self.match(BKITParser.CONTINUE)
            self.state = 289
            self.match(BKITParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Call_stmContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(BKITParser.ID, 0)

        def LB(self):
            return self.getToken(BKITParser.LB, 0)

        def RB(self):
            return self.getToken(BKITParser.RB, 0)

        def SEMI(self):
            return self.getToken(BKITParser.SEMI, 0)

        def call_stm_para_list(self):
            return self.getTypedRuleContext(BKITParser.Call_stm_para_listContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_call_stm

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCall_stm" ):
                return visitor.visitCall_stm(self)
            else:
                return visitor.visitChildren(self)




    def call_stm(self):

        localctx = BKITParser.Call_stmContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_call_stm)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 291
            self.match(BKITParser.ID)
            self.state = 292
            self.match(BKITParser.LB)
            self.state = 294
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKITParser.ID) | (1 << BKITParser.INTSUB) | (1 << BKITParser.FLOATSUB) | (1 << BKITParser.NEG) | (1 << BKITParser.INTLIT) | (1 << BKITParser.FLOATLIT) | (1 << BKITParser.BOOLEANLIT) | (1 << BKITParser.STRING_LIT))) != 0):
                self.state = 293
                self.call_stm_para_list()


            self.state = 296
            self.match(BKITParser.RB)
            self.state = 297
            self.match(BKITParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Call_stm_para_listContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp(self):
            return self.getTypedRuleContext(BKITParser.ExpContext,0)


        def COMMA(self):
            return self.getToken(BKITParser.COMMA, 0)

        def call_stm_para_list(self):
            return self.getTypedRuleContext(BKITParser.Call_stm_para_listContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_call_stm_para_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCall_stm_para_list" ):
                return visitor.visitCall_stm_para_list(self)
            else:
                return visitor.visitChildren(self)




    def call_stm_para_list(self):

        localctx = BKITParser.Call_stm_para_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_call_stm_para_list)
        try:
            self.state = 304
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,26,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 299
                self.exp()
                self.state = 300
                self.match(BKITParser.COMMA)
                self.state = 301
                self.call_stm_para_list()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 303
                self.exp()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Return_stmContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RETURN(self):
            return self.getToken(BKITParser.RETURN, 0)

        def SEMI(self):
            return self.getToken(BKITParser.SEMI, 0)

        def exp(self):
            return self.getTypedRuleContext(BKITParser.ExpContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_return_stm

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReturn_stm" ):
                return visitor.visitReturn_stm(self)
            else:
                return visitor.visitChildren(self)




    def return_stm(self):

        localctx = BKITParser.Return_stmContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_return_stm)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 306
            self.match(BKITParser.RETURN)
            self.state = 308
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKITParser.ID) | (1 << BKITParser.INTSUB) | (1 << BKITParser.FLOATSUB) | (1 << BKITParser.NEG) | (1 << BKITParser.INTLIT) | (1 << BKITParser.FLOATLIT) | (1 << BKITParser.BOOLEANLIT) | (1 << BKITParser.STRING_LIT))) != 0):
                self.state = 307
                self.exp()


            self.state = 310
            self.match(BKITParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Relational_opContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INTEQUAL(self):
            return self.getToken(BKITParser.INTEQUAL, 0)

        def INTNOTEQUAL(self):
            return self.getToken(BKITParser.INTNOTEQUAL, 0)

        def INTLESS(self):
            return self.getToken(BKITParser.INTLESS, 0)

        def INTGREATER(self):
            return self.getToken(BKITParser.INTGREATER, 0)

        def INTLESSEQUAL(self):
            return self.getToken(BKITParser.INTLESSEQUAL, 0)

        def INTGREATEREQUAL(self):
            return self.getToken(BKITParser.INTGREATEREQUAL, 0)

        def FLNOTEQUAL(self):
            return self.getToken(BKITParser.FLNOTEQUAL, 0)

        def FLLESS(self):
            return self.getToken(BKITParser.FLLESS, 0)

        def FLGREATER(self):
            return self.getToken(BKITParser.FLGREATER, 0)

        def FLLESSEQUAL(self):
            return self.getToken(BKITParser.FLLESSEQUAL, 0)

        def FLGREATEREQUAL(self):
            return self.getToken(BKITParser.FLGREATEREQUAL, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_relational_op

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRelational_op" ):
                return visitor.visitRelational_op(self)
            else:
                return visitor.visitChildren(self)




    def relational_op(self):

        localctx = BKITParser.Relational_opContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_relational_op)
        try:
            self.state = 324
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKITParser.ID, BKITParser.INTSUB, BKITParser.FLOATSUB, BKITParser.NEG, BKITParser.INTLIT, BKITParser.FLOATLIT, BKITParser.BOOLEANLIT, BKITParser.STRING_LIT]:
                self.enterOuterAlt(localctx, 1)

                pass
            elif token in [BKITParser.INTEQUAL]:
                self.enterOuterAlt(localctx, 2)
                self.state = 313
                self.match(BKITParser.INTEQUAL)
                pass
            elif token in [BKITParser.INTNOTEQUAL]:
                self.enterOuterAlt(localctx, 3)
                self.state = 314
                self.match(BKITParser.INTNOTEQUAL)
                pass
            elif token in [BKITParser.INTLESS]:
                self.enterOuterAlt(localctx, 4)
                self.state = 315
                self.match(BKITParser.INTLESS)
                pass
            elif token in [BKITParser.INTGREATER]:
                self.enterOuterAlt(localctx, 5)
                self.state = 316
                self.match(BKITParser.INTGREATER)
                pass
            elif token in [BKITParser.INTLESSEQUAL]:
                self.enterOuterAlt(localctx, 6)
                self.state = 317
                self.match(BKITParser.INTLESSEQUAL)
                pass
            elif token in [BKITParser.INTGREATEREQUAL]:
                self.enterOuterAlt(localctx, 7)
                self.state = 318
                self.match(BKITParser.INTGREATEREQUAL)
                pass
            elif token in [BKITParser.FLNOTEQUAL]:
                self.enterOuterAlt(localctx, 8)
                self.state = 319
                self.match(BKITParser.FLNOTEQUAL)
                pass
            elif token in [BKITParser.FLLESS]:
                self.enterOuterAlt(localctx, 9)
                self.state = 320
                self.match(BKITParser.FLLESS)
                pass
            elif token in [BKITParser.FLGREATER]:
                self.enterOuterAlt(localctx, 10)
                self.state = 321
                self.match(BKITParser.FLGREATER)
                pass
            elif token in [BKITParser.FLLESSEQUAL]:
                self.enterOuterAlt(localctx, 11)
                self.state = 322
                self.match(BKITParser.FLLESSEQUAL)
                pass
            elif token in [BKITParser.FLGREATEREQUAL]:
                self.enterOuterAlt(localctx, 12)
                self.state = 323
                self.match(BKITParser.FLGREATEREQUAL)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Logical_opContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CONJUNC(self):
            return self.getToken(BKITParser.CONJUNC, 0)

        def DISJUNC(self):
            return self.getToken(BKITParser.DISJUNC, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_logical_op

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLogical_op" ):
                return visitor.visitLogical_op(self)
            else:
                return visitor.visitChildren(self)




    def logical_op(self):

        localctx = BKITParser.Logical_opContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_logical_op)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 326
            _la = self._input.LA(1)
            if not(_la==BKITParser.CONJUNC or _la==BKITParser.DISJUNC):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Adding_opContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INTADD(self):
            return self.getToken(BKITParser.INTADD, 0)

        def FLOATADD(self):
            return self.getToken(BKITParser.FLOATADD, 0)

        def INTSUB(self):
            return self.getToken(BKITParser.INTSUB, 0)

        def FLOATSUB(self):
            return self.getToken(BKITParser.FLOATSUB, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_adding_op

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAdding_op" ):
                return visitor.visitAdding_op(self)
            else:
                return visitor.visitChildren(self)




    def adding_op(self):

        localctx = BKITParser.Adding_opContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_adding_op)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 328
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKITParser.INTADD) | (1 << BKITParser.FLOATADD) | (1 << BKITParser.INTSUB) | (1 << BKITParser.FLOATSUB))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Multiplying_opContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INTMUL(self):
            return self.getToken(BKITParser.INTMUL, 0)

        def FLOATMUL(self):
            return self.getToken(BKITParser.FLOATMUL, 0)

        def INTDIV(self):
            return self.getToken(BKITParser.INTDIV, 0)

        def FLOATDIV(self):
            return self.getToken(BKITParser.FLOATDIV, 0)

        def INTREMAINDER(self):
            return self.getToken(BKITParser.INTREMAINDER, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_multiplying_op

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMultiplying_op" ):
                return visitor.visitMultiplying_op(self)
            else:
                return visitor.visitChildren(self)




    def multiplying_op(self):

        localctx = BKITParser.Multiplying_opContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_multiplying_op)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 330
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKITParser.INTMUL) | (1 << BKITParser.FLOATMUL) | (1 << BKITParser.INTDIV) | (1 << BKITParser.FLOATDIV) | (1 << BKITParser.INTREMAINDER))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp1(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKITParser.Exp1Context)
            else:
                return self.getTypedRuleContext(BKITParser.Exp1Context,i)


        def relational_op(self):
            return self.getTypedRuleContext(BKITParser.Relational_opContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_exp

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp" ):
                return visitor.visitExp(self)
            else:
                return visitor.visitChildren(self)




    def exp(self):

        localctx = BKITParser.ExpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_exp)
        try:
            self.state = 337
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,29,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 332
                self.exp1(0)
                self.state = 333
                self.relational_op()
                self.state = 334
                self.exp1(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 336
                self.exp1(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Exp1Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp2(self):
            return self.getTypedRuleContext(BKITParser.Exp2Context,0)


        def exp1(self):
            return self.getTypedRuleContext(BKITParser.Exp1Context,0)


        def logical_op(self):
            return self.getTypedRuleContext(BKITParser.Logical_opContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_exp1

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp1" ):
                return visitor.visitExp1(self)
            else:
                return visitor.visitChildren(self)



    def exp1(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = BKITParser.Exp1Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 66
        self.enterRecursionRule(localctx, 66, self.RULE_exp1, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 340
            self.exp2(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 348
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,30,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = BKITParser.Exp1Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_exp1)
                    self.state = 342
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 343
                    self.logical_op()
                    self.state = 344
                    self.exp2(0) 
                self.state = 350
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,30,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Exp2Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp3(self):
            return self.getTypedRuleContext(BKITParser.Exp3Context,0)


        def exp2(self):
            return self.getTypedRuleContext(BKITParser.Exp2Context,0)


        def adding_op(self):
            return self.getTypedRuleContext(BKITParser.Adding_opContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_exp2

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp2" ):
                return visitor.visitExp2(self)
            else:
                return visitor.visitChildren(self)



    def exp2(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = BKITParser.Exp2Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 68
        self.enterRecursionRule(localctx, 68, self.RULE_exp2, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 352
            self.exp3(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 360
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,31,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = BKITParser.Exp2Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_exp2)
                    self.state = 354
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 355
                    self.adding_op()
                    self.state = 356
                    self.exp3(0) 
                self.state = 362
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,31,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Exp3Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp4(self):
            return self.getTypedRuleContext(BKITParser.Exp4Context,0)


        def exp3(self):
            return self.getTypedRuleContext(BKITParser.Exp3Context,0)


        def multiplying_op(self):
            return self.getTypedRuleContext(BKITParser.Multiplying_opContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_exp3

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp3" ):
                return visitor.visitExp3(self)
            else:
                return visitor.visitChildren(self)



    def exp3(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = BKITParser.Exp3Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 70
        self.enterRecursionRule(localctx, 70, self.RULE_exp3, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 364
            self.exp4()
            self._ctx.stop = self._input.LT(-1)
            self.state = 372
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,32,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = BKITParser.Exp3Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_exp3)
                    self.state = 366
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 367
                    self.multiplying_op()
                    self.state = 368
                    self.exp4() 
                self.state = 374
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,32,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Exp4Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NEG(self):
            return self.getToken(BKITParser.NEG, 0)

        def exp4(self):
            return self.getTypedRuleContext(BKITParser.Exp4Context,0)


        def exp5(self):
            return self.getTypedRuleContext(BKITParser.Exp5Context,0)


        def getRuleIndex(self):
            return BKITParser.RULE_exp4

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp4" ):
                return visitor.visitExp4(self)
            else:
                return visitor.visitChildren(self)




    def exp4(self):

        localctx = BKITParser.Exp4Context(self, self._ctx, self.state)
        self.enterRule(localctx, 72, self.RULE_exp4)
        try:
            self.state = 378
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKITParser.NEG]:
                self.enterOuterAlt(localctx, 1)
                self.state = 375
                self.match(BKITParser.NEG)
                self.state = 376
                self.exp4()
                pass
            elif token in [BKITParser.ID, BKITParser.INTSUB, BKITParser.FLOATSUB, BKITParser.INTLIT, BKITParser.FLOATLIT, BKITParser.BOOLEANLIT, BKITParser.STRING_LIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 377
                self.exp5()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Exp5Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp5(self):
            return self.getTypedRuleContext(BKITParser.Exp5Context,0)


        def INTSUB(self):
            return self.getToken(BKITParser.INTSUB, 0)

        def FLOATSUB(self):
            return self.getToken(BKITParser.FLOATSUB, 0)

        def exp6(self):
            return self.getTypedRuleContext(BKITParser.Exp6Context,0)


        def getRuleIndex(self):
            return BKITParser.RULE_exp5

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp5" ):
                return visitor.visitExp5(self)
            else:
                return visitor.visitChildren(self)




    def exp5(self):

        localctx = BKITParser.Exp5Context(self, self._ctx, self.state)
        self.enterRule(localctx, 74, self.RULE_exp5)
        self._la = 0 # Token type
        try:
            self.state = 383
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,34,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 380
                _la = self._input.LA(1)
                if not(_la==BKITParser.INTSUB or _la==BKITParser.FLOATSUB):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 381
                self.exp5()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 382
                self.exp6(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Exp6Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp7(self):
            return self.getTypedRuleContext(BKITParser.Exp7Context,0)


        def exp6(self):
            return self.getTypedRuleContext(BKITParser.Exp6Context,0)


        def index_operators(self):
            return self.getTypedRuleContext(BKITParser.Index_operatorsContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_exp6

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp6" ):
                return visitor.visitExp6(self)
            else:
                return visitor.visitChildren(self)



    def exp6(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = BKITParser.Exp6Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 76
        self.enterRecursionRule(localctx, 76, self.RULE_exp6, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 386
            self.exp7()
            self._ctx.stop = self._input.LT(-1)
            self.state = 392
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,35,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = BKITParser.Exp6Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_exp6)
                    self.state = 388
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 389
                    self.index_operators() 
                self.state = 394
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,35,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Index_operatorsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LSB(self):
            return self.getToken(BKITParser.LSB, 0)

        def exp(self):
            return self.getTypedRuleContext(BKITParser.ExpContext,0)


        def RSB(self):
            return self.getToken(BKITParser.RSB, 0)

        def index_operators(self):
            return self.getTypedRuleContext(BKITParser.Index_operatorsContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_index_operators

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIndex_operators" ):
                return visitor.visitIndex_operators(self)
            else:
                return visitor.visitChildren(self)




    def index_operators(self):

        localctx = BKITParser.Index_operatorsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 78, self.RULE_index_operators)
        try:
            self.state = 404
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,36,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 395
                self.match(BKITParser.LSB)
                self.state = 396
                self.exp()
                self.state = 397
                self.match(BKITParser.RSB)
                self.state = 398
                self.index_operators()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 400
                self.match(BKITParser.LSB)
                self.state = 401
                self.exp()
                self.state = 402
                self.match(BKITParser.RSB)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Exp7Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(BKITParser.ID, 0)

        def LB(self):
            return self.getToken(BKITParser.LB, 0)

        def call_stm_para_list(self):
            return self.getTypedRuleContext(BKITParser.Call_stm_para_listContext,0)


        def RB(self):
            return self.getToken(BKITParser.RB, 0)

        def operand(self):
            return self.getTypedRuleContext(BKITParser.OperandContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_exp7

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp7" ):
                return visitor.visitExp7(self)
            else:
                return visitor.visitChildren(self)




    def exp7(self):

        localctx = BKITParser.Exp7Context(self, self._ctx, self.state)
        self.enterRule(localctx, 80, self.RULE_exp7)
        try:
            self.state = 413
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,37,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 406
                self.match(BKITParser.ID)
                self.state = 407
                self.match(BKITParser.LB)
                self.state = 408
                self.call_stm_para_list()
                self.state = 409
                self.match(BKITParser.RB)
                self.state = 410
                self.operand()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 412
                self.operand()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OperandContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def constants(self):
            return self.getTypedRuleContext(BKITParser.ConstantsContext,0)


        def variable(self):
            return self.getTypedRuleContext(BKITParser.VariableContext,0)


        def ID(self):
            return self.getToken(BKITParser.ID, 0)

        def LB(self):
            return self.getToken(BKITParser.LB, 0)

        def RB(self):
            return self.getToken(BKITParser.RB, 0)

        def call_stm_para_list(self):
            return self.getTypedRuleContext(BKITParser.Call_stm_para_listContext,0)


        def literal(self):
            return self.getTypedRuleContext(BKITParser.LiteralContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_operand

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOperand" ):
                return visitor.visitOperand(self)
            else:
                return visitor.visitChildren(self)




    def operand(self):

        localctx = BKITParser.OperandContext(self, self._ctx, self.state)
        self.enterRule(localctx, 82, self.RULE_operand)
        self._la = 0 # Token type
        try:
            self.state = 424
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,39,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 415
                self.constants()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 416
                self.variable()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 417
                self.match(BKITParser.ID)
                self.state = 418
                self.match(BKITParser.LB)
                self.state = 420
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKITParser.ID) | (1 << BKITParser.INTSUB) | (1 << BKITParser.FLOATSUB) | (1 << BKITParser.NEG) | (1 << BKITParser.INTLIT) | (1 << BKITParser.FLOATLIT) | (1 << BKITParser.BOOLEANLIT) | (1 << BKITParser.STRING_LIT))) != 0):
                    self.state = 419
                    self.call_stm_para_list()


                self.state = 422
                self.match(BKITParser.RB)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 423
                self.literal()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConstantsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def literal(self):
            return self.getTypedRuleContext(BKITParser.LiteralContext,0)


        def INTSUB(self):
            return self.getToken(BKITParser.INTSUB, 0)

        def FLOATSUB(self):
            return self.getToken(BKITParser.FLOATSUB, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_constants

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConstants" ):
                return visitor.visitConstants(self)
            else:
                return visitor.visitChildren(self)




    def constants(self):

        localctx = BKITParser.ConstantsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 84, self.RULE_constants)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 427
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BKITParser.INTSUB or _la==BKITParser.FLOATSUB:
                self.state = 426
                _la = self._input.LA(1)
                if not(_la==BKITParser.INTSUB or _la==BKITParser.FLOATSUB):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()


            self.state = 429
            self.literal()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LiteralContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INTLIT(self):
            return self.getToken(BKITParser.INTLIT, 0)

        def FLOATLIT(self):
            return self.getToken(BKITParser.FLOATLIT, 0)

        def STRING_LIT(self):
            return self.getToken(BKITParser.STRING_LIT, 0)

        def BOOLEANLIT(self):
            return self.getToken(BKITParser.BOOLEANLIT, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_literal

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLiteral" ):
                return visitor.visitLiteral(self)
            else:
                return visitor.visitChildren(self)




    def literal(self):

        localctx = BKITParser.LiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 86, self.RULE_literal)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 431
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKITParser.INTLIT) | (1 << BKITParser.FLOATLIT) | (1 << BKITParser.BOOLEANLIT) | (1 << BKITParser.STRING_LIT))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[33] = self.exp1_sempred
        self._predicates[34] = self.exp2_sempred
        self._predicates[35] = self.exp3_sempred
        self._predicates[38] = self.exp6_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def exp1_sempred(self, localctx:Exp1Context, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 2)
         

    def exp2_sempred(self, localctx:Exp2Context, predIndex:int):
            if predIndex == 1:
                return self.precpred(self._ctx, 2)
         

    def exp3_sempred(self, localctx:Exp3Context, predIndex:int):
            if predIndex == 2:
                return self.precpred(self._ctx, 2)
         

    def exp6_sempred(self, localctx:Exp6Context, predIndex:int):
            if predIndex == 3:
                return self.precpred(self._ctx, 2)
         




