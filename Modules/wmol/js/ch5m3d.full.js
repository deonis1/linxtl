//
// -------------------- periodic.js --------------------
//
//  Authors: Clarke Earley, Denis Spasyuk
//#   function element(Z,param)
//#
//#   Define public routine to store and return elemental information
//#
//#   Parameters:
//#      Z = Atomic number of element
//#      param:
//#         symbol   - Elemental symbol
//#         block    - "s", "p", "d", or "f" block 
//#         valence  - # of valence electrons
//#         mass     - Atomic mass
//#         radius   - Covalent radius of atom
//#         EN       - Electronegativity of atom
//#         color    - color of atom (based on JMol)
//#         gradient - gradient color for atom
//#         label    - color for label
//#
//#   Return value:
//#      Variable containing requested information
//#
function element(Z,param) {
  if ( typeof element.elem == 'undefined' ) {
    element.elem = [];
    //
    //  Load parameters for all elements
    //
    //  Parameters:
    //    Atomic number
    //    Element symbol
    //    Block (s, p, d, or f)
    //    Number of valence electrons
    //    Atomic mass
    //    Covalent radii (in pm).  From www.webelements.com
    //    Jmol CPK colors (rgb).  From jmol.sourceforge.net/jscolors/
    //    Electronegativities from Wikipedia, citing WebElements as their source
    //
    element.elem[0]  = addElement(0, 'X', 's', 0, 0, 0, 0, 0, 0, 0);
    element.elem[1]  = addElement(1, 'H', 's', 1, 1.0079, 31, 255, 255, 255, 2.2);
    element.elem[2]  = addElement(2, 'He', 's', 2, 4.0026, 28, 217, 255, 255, 0);
    element.elem[3]  = addElement(3, 'Li', 's', 1, 6.941, 128, 204, 128, 255, 0.98);
    element.elem[4]  = addElement(4, 'Be', 's', 2, 9.0122, 96, 194, 255, 0, 1.57);
    element.elem[5]  = addElement(5, 'B', 'p', 4, 10.811, 84, 255, 181, 181, 2.04);
    element.elem[6]  = addElement(6, 'C', 'p', 4, 12.0107, 76, 50, 50, 50, 2.55);
    element.elem[7]  = addElement(7, 'N', 'p', 5, 14.0067, 71, 48, 80, 248, 3.04);
    element.elem[8]  = addElement(8, 'O', 'p', 6, 15.9994, 66, 255, 13, 13, 3.44);
    element.elem[9]  = addElement(9, 'F', 'p', 7, 18.9984, 57, 144, 224, 80, 3.98);
    element.elem[10] = addElement(10, 'Ne', 'p', 8, 20.1797, 58, 179, 227, 245, 0);
    element.elem[11] = addElement(11, 'Na', 's', 1, 22.9897, 166, 171, 92, 242, 0.93);
    element.elem[12] = addElement(12, 'Mg', 's', 2, 24.305, 141, 138, 255, 0, 1.31);
    element.elem[13] = addElement(13, 'Al', 'p', 3, 26.9815, 121, 191, 166, 166, 1.61);
    element.elem[14] = addElement(14, 'Si', 'p', 4, 28.0855, 111, 240, 200, 160, 1.9);
    element.elem[15] = addElement(15, 'P', 'p', 5, 30.9738, 107, 255, 128, 0, 2.19);
    element.elem[16] = addElement(16, 'S', 'p', 6, 32.065, 105, 255, 255, 48, 2.58);
    element.elem[17] = addElement(17, 'Cl', 'p', 7, 35.453, 102, 31, 240, 31, 3.16);
    element.elem[18] = addElement(18, 'Ar', 'p', 8, 39.948, 106, 128, 209, 227, 0);
    element.elem[19] = addElement(19, 'K', 's', 1, 39.0983, 203, 143, 64, 212, 0.82);
    element.elem[20] = addElement(20, 'Ca', 's', 2, 40.078, 176, 61, 255, 0, 1);
    element.elem[21] = addElement(21, 'Sc', 'd', 3, 44.9559, 170, 230, 230, 230, 1.36);
    element.elem[22] = addElement(22, 'Ti', 'd', 4, 47.867, 160, 191, 194, 199, 1.54);
    element.elem[23] = addElement(23, 'V', 'd', 5, 50.9415, 153, 166, 166, 171, 1.63);
    element.elem[24] = addElement(24, 'Cr', 'd', 6, 51.9961, 139, 138, 153, 199, 1.66);
    element.elem[25] = addElement(25, 'Mn', 'd', 7, 54.938, 139, 156, 122, 199, 1.55);
    element.elem[26] = addElement(26, 'Fe', 'd', 8, 55.845, 132, 224, 102, 51, 1.83);
    element.elem[27] = addElement(27, 'Co', 'd', 9, 58.9332, 126, 240, 144, 160, 1.88);
    element.elem[28] = addElement(28, 'Ni', 'd', 10, 58.6934, 124, 80, 208, 80, 1.91);
    element.elem[29] = addElement(29, 'Cu', 'd', 11, 63.546, 132, 200, 128, 51, 1.9);
    element.elem[30] = addElement(30, 'Zn', 'd', 2, 65.39, 122, 125, 128, 176, 1.65);
    element.elem[31] = addElement(31, 'Ga', 'p', 3, 69.723, 122, 194, 143, 143, 1.81);
    element.elem[32] = addElement(32, 'Ge', 'p', 4, 72.64, 120, 102, 143, 143, 2.01);
    element.elem[33] = addElement(33, 'As', 'p', 5, 74.9216, 119, 189, 128, 227, 2.18);
    element.elem[34] = addElement(34, 'Se', 'p', 6, 78.96, 120, 255, 161, 0, 2.55);
    element.elem[35] = addElement(35, 'Br', 'p', 7, 79.904, 120, 166, 41, 41, 2.96);
    element.elem[36] = addElement(36, 'Kr', 'p', 8, 83.8, 116, 92, 184, 209, 3);
    element.elem[37] = addElement(37, 'Rb', 's', 1, 85.4678, 220, 112, 46, 176, 0.82);
    element.elem[38] = addElement(38, 'Sr', 's', 2, 87.62, 195, 0, 255, 0, 0.95);
    element.elem[39] = addElement(39, 'Y', 'd', 3, 88.9059, 190, 148, 255, 255, 1.22);
    element.elem[40] = addElement(40, 'Zr', 'd', 4, 91.224, 175, 148, 224, 224, 1.33);
    element.elem[41] = addElement(41, 'Nb', 'd', 5, 92.9064, 164, 115, 194, 201, 1.6);
    element.elem[42] = addElement(42, 'Mo', 'd', 6, 95.94, 154, 84, 181, 181, 2.16);
    element.elem[43] = addElement(43, 'Tc', 'd', 7, 98, 147, 59, 158, 158, 1.9);
    element.elem[44] = addElement(44, 'Ru', 'd', 8, 101.07, 146, 36, 143, 143, 2.2);
    element.elem[45] = addElement(45, 'Rh', 'd', 9, 102.9055, 142, 10, 125, 140, 2.28);
    element.elem[46] = addElement(46, 'Pd', 'd', 10, 106.42, 139, 0, 105, 133, 2.2);
    element.elem[47] = addElement(47, 'Ag', 'd', 11, 107.8682, 145, 192, 192, 192, 1.93);
    element.elem[48] = addElement(48, 'Cd', 'd', 2, 112.411, 144, 255, 217, 143, 1.69);
    element.elem[49] = addElement(49, 'In', 'p', 3, 114.818, 142, 166, 117, 115, 1.78);
    element.elem[50] = addElement(50, 'Sn', 'p', 4, 118.71, 139, 102, 128, 128, 1.96);
    element.elem[51] = addElement(51, 'Sb', 'p', 5, 121.76, 139, 158, 99, 181, 2.05);
    element.elem[52] = addElement(52, 'Te', 'p', 6, 127.6, 138, 212, 122, 0, 2.1);
    element.elem[53] = addElement(53, 'I', 'p', 7, 126.9045, 139, 148, 0, 148, 2.66);
    element.elem[54] = addElement(54, 'Xe', 'p', 8, 131.293, 140, 66, 158, 176, 2.6);
    element.elem[55] = addElement(55, 'Cs', 's', 1, 132.9055, 244, 87, 23, 143, 0.79);
    element.elem[56] = addElement(56, 'Ba', 's', 2, 137.327, 215, 0, 201, 0, 0.89);
    element.elem[57] = addElement(57, 'La', 'd', 3, 138.9055, 207, 112, 212, 255, 1.1);
    element.elem[58] = addElement(58, 'Ce', 'f', 4, 140.116, 204, 255, 255, 199, 1.12);
    element.elem[59] = addElement(59, 'Pr', 'f', 5, 140.9077, 203, 217, 255, 199, 1.13);
    element.elem[60] = addElement(60, 'Nd', 'f', 6, 144.24, 201, 199, 255, 199, 1.14);
    element.elem[61] = addElement(61, 'Pm', 'f', 7, 145, 199, 163, 255, 199, 0);
    element.elem[62] = addElement(62, 'Sm', 'f', 8, 150.36, 198, 143, 255, 199, 1.17);
    element.elem[63] = addElement(63, 'Eu', 'f', 9, 151.964, 198, 97, 255, 199, 0);
    element.elem[64] = addElement(64, 'Gd', 'f', 10, 157.25, 196, 69, 255, 199, 1.2);
    element.elem[65] = addElement(65, 'Tb', 'f', 11, 158.9253, 194, 48, 255, 199, 0);
    element.elem[66] = addElement(66, 'Dy', 'f', 12, 162.5, 192, 31, 255, 199, 1.22);
    element.elem[67] = addElement(67, 'Ho', 'f', 13, 164.9303, 192, 0, 255, 156, 1.23);
    element.elem[68] = addElement(68, 'Er', 'f', 14, 167.259, 189, 0, 230, 117, 1.24);
    element.elem[69] = addElement(69, 'Tm', 'f', 15, 168.9342, 190, 0, 212, 82, 1.25);
    element.elem[70] = addElement(70, 'Yb', 'f', 16, 173.04, 187, 0, 191, 56, 0);
    element.elem[71] = addElement(71, 'Lu', 'f', 17, 174.967, 187, 0, 171, 36, 1.27);
    element.elem[72] = addElement(72, 'Hf', 'd', 4, 178.49, 175, 77, 194, 255, 1.3);
    element.elem[73] = addElement(73, 'Ta', 'd', 5, 180.9479, 170, 77, 166, 255, 1.5);
    element.elem[74] = addElement(74, 'W', 'd', 6, 183.84, 162, 33, 148, 214, 2.36);
    element.elem[75] = addElement(75, 'Re', 'd', 7, 186.207, 151, 38, 125, 171, 1.9);
    element.elem[76] = addElement(76, 'Os', 'd', 8, 190.23, 144, 38, 102, 150, 2.2);
    element.elem[77] = addElement(77, 'Ir', 'd', 9, 192.217, 141, 23, 84, 135, 2.2);
    element.elem[78] = addElement(78, 'Pt', 'd', 10, 195.078, 136, 208, 208, 224, 2.28);
    element.elem[79] = addElement(79, 'Au', 'd', 11, 196.9665, 136, 255, 209, 35, 2.54);
    element.elem[80] = addElement(80, 'Hg', 'd', 2, 200.59, 132, 184, 184, 208, 2);
    element.elem[81] = addElement(81, 'Tl', 'p', 3, 204.3833, 145, 166, 84, 77, 1.62);
    element.elem[82] = addElement(82, 'Pb', 'p', 4, 207.2, 146, 87, 89, 97, 2.33);
    element.elem[83] = addElement(83, 'Bi', 'p', 5, 208.9804, 148, 158, 79, 181, 2.02);
    element.elem[84] = addElement(84, 'Po', 'p', 6, 209, 140, 171, 92, 0, 2);
    element.elem[85] = addElement(85, 'At', 'p', 7, 210, 150, 117, 79, 69, 2.2);
    element.elem[86] = addElement(86, 'Rn', 'p', 8, 222, 150, 66, 130, 150, 0);
    element.elem[87] = addElement(87, 'Fr', 's', 1, 223, 260, 66, 0, 102, 0.7);
    element.elem[88] = addElement(88, 'Ra', 's', 2, 226, 221, 0, 125, 0, 0.9);
    element.elem[89] = addElement(89, 'Ac', 'd', 3, 227, 215, 112, 171, 250, 1.1);
    element.elem[90] = addElement(90, 'Th', 'f', 4, 232.0381, 206, 0, 186, 255, 1.3);
    element.elem[91] = addElement(91, 'Pa', 'f', 5, 231.0359, 200, 0, 161, 255, 1.5);
    element.elem[92] = addElement(92, 'U', 'f', 6, 238.0289, 196, 0, 143, 255, 1.38);
    element.elem[93] = addElement(93, 'Np', 'f', 7, 237, 190, 0, 128, 255, 1.36);
    element.elem[94] = addElement(94, 'Pu', 'f', 8, 244, 187, 0, 107, 255, 1.28);
    element.elem[95] = addElement(95, 'Am', 'f', 9, 243, 180, 84, 92, 242, 1.3);
    element.elem[96] = addElement(96, 'Cm', 'f', 10, 247, 169, 120, 92, 227, 1.3);
    element.elem[97] = addElement(97, 'Bk', 'f', 11, 247, 168, 138, 79, 227, 1.3);
    element.elem[98] = addElement(98, 'Cf', 'f', 12, 251, 168, 161, 54, 212, 1.3);
    element.elem[99] = addElement(99, 'Es', 'f', 13, 252, 165, 179, 31, 212, 1.3);
    element.elem[100] = addElement(100, 'Fm', 'f', 14, 257, 167, 179, 31, 186, 1.3);
    element.elem[101] = addElement(101, 'Md', 'f', 15, 258, 173, 179, 13, 166, 1.3);
    element.elem[102] = addElement(102, 'No', 'f', 16, 259, 176, 189, 13, 135, 1.3);
    element.elem[103] = addElement(103, 'Lr', 'f', 17, 262, 161, 199, 0, 102, 0);
    element.elem[104] = addElement(104, 'Rf', 'd', 4, 267, 157, 204, 0, 89, 0);
    element.elem[105] = addElement(105, 'Db', 'd', 5, 268, 149, 209, 0, 79, 0);
    element.elem[106] = addElement(106, 'Sg', 'd', 6, 269, 143, 217, 0, 69, 0);
    element.elem[107] = addElement(107, 'Bh', 'd', 7, 270, 141, 224, 0, 56, 0);
    element.elem[108] = addElement(108, 'Hs', 'd', 8, 269, 134, 230, 0, 46, 0);
    element.elem[109] = addElement(109, 'Mt', 'd', 9, 278, 129, 235, 0, 38, 0);
    element.elem[110] = addElement(110, 'Ds', 'd', 10, 281, 0, 0, 0, 28, 0);
    element.elem[111] = addElement(111, 'Rg', 'd', 11, 281, 0, 0, 0, 28, 0);
    element.elem[112] = addElement(112, 'Cn', 'd', 12, 285, 0, 0, 0, 28, 0);
    element.elem[113] = addElement(113, 'Uut', 'p', 3, 286, 0, 0, 0, 28, 0);
    element.elem[114] = addElement(114, 'Fl', 'p', 4, 289, 0, 0, 0, 28, 0);
    element.elem[115] = addElement(115, 'Uup', 'p', 5, 288, 0, 0, 0, 28, 0);
    element.elem[116] = addElement(116, 'Lv', 'p', 6, 293, 0, 0, 0, 28, 0);
    element.elem[117] = addElement(117, 'Uus', 'p', 7, 294, 0, 0, 0, 28, 0);
    element.elem[118] = addElement(118, 'Uuo', 'p', 8, 294, 0, 0, 0, 28, 0);
    }

  // Make sure element requested is defined.
  if ( (Z < 0)  ||  (Z > element.elem.length) ) {
    alert("Element "+Z+" is not defined.");
    return 0;
    }

  // Determine what information is requested and return value
  switch (param) {
    case "symbol":
        return element.elem[Z].symbol;
        break;
    case "block":
        return element.elem[Z].block;
        break;
    case "valence":
        return element.elem[Z].valence;
        break;
    case "mass":
        return element.elem[Z].mass;
        break;
    case "radius":
        return element.elem[Z].radius;
        break;
    case "EN":
        return element.elem[Z].EN;
        break;
    case "color":
        return element.elem[Z].color;
        break;
    case "gradient":
        return element.elem[Z].gradient;
        break;
    case "label":
        return element.elem[Z].label;
        break;
    case "max":
        return element.elem.length;
        break;
    default:
        alert("Param "+param+" is not defined.");
        return 0;
        break;
    }
  // End of element routine
  }


///
///   Define internal structure for elemental information
///
function elementObject() {
  this.symbol = "?";
  this.block = "?";
  this.valence = 0;
  this.mass = 0.0;
  this.radius = 0.0;
  this.EN = 0.0;
  this.color   = "rgb(88,88,88)";
  this.gradient = "rgb(88,88,88)";
  this.label = "rgb(255,255,255)";
  }


///
///   Internal routine to add information for elements
///
// Adds shades to atoms
function addElement(Z, Symbol, block, valence, mass, radius, red, green, blue, EN)  {

  // Declare local variables
  var atomR, sum;
  var element = new elementObject();

  // Add elemental information
  element.symbol = Symbol;
  element.block = block;
  element.valence = valence;
  element.mass = mass;
  (radius <= 0) ? atomR = 0.1 : atomR = radius / 100.0;
  element.radius = atomR;
  //element.blur = 50
  element.color = "rgb("+red+","+green+","+blue+")";
  element.gradient = "rgb("+Math.floor(red/4)+","+Math.floor(green/4)+","+Math.floor(blue/4)+")";
  sum = red + green + blue;
  element.label = (sum > 384) ? "rgb(0,0,0)" : "rgb(255,255,255)";  
  element.EN = EN;

  // End of addElement routine
  return element;
  }


//#   function drawPeriodic()
//#
//#   Writes html code to a division named "ptable".  The periodic table is written as a table, and each element
//#   is linked to to the pickElem() routine.
//#
function drawPeriodic()  {

  // Declare local variables
  var html;
  var PerDivision = "ptable";

  html  = "<table><tr>";
  html += "<td class=\"main\" id=\"mH\"  onclick=\"pickElem('H');\">H</td>";
  html += "<td class=\"Row\"  id=\"Row1\" colspan=\"12\">&nbsp;</td>";
//  html += "<td class=\"MOff\" id=\"MOff\" colspan=\"2\" onclick=\"pickElem('MOff');\">Main</td>";
//  html += "<td class=\"MOn\"  id=\"MOn\"  colspan=\"2\" onclick=\"pickElem('MOn');\">Metals</td>";
  html += "<td class=\"plabel\" id=\"plabel\" colspan=\"4\" onclick=\"pickElem('PView');\">";
  html += "<div id=\"pchooser\">Metals</div></td>";
  html += "<td class=\"metl\" id=\"pHe\" onclick=\"pickElem('He');\">He</td>";
  html += "</tr>\n";

  html += "<tr>";
  html += "<td class=\"metl\" id=\"pLi\" onclick=\"pickElem('Li');\">Li</td>";
  html += "<td class=\"metl\" id=\"pBe\" onclick=\"pickElem('Be');\">Be</td>";
  html += "<td class=\"Row\"  id=\"Row2\" colspan=\"10\">&nbsp;</td>";
  html += "<td class=\"main\" id=\"mB\"  onclick=\"pickElem('B');\">B</td>";
  html += "<td class=\"main\" id=\"mC\"  onclick=\"pickElem('C');\">C</td>";
  html += "<td class=\"main\" id=\"mN\"  onclick=\"pickElem('N');\">N</td>";
  html += "<td class=\"main\" id=\"mO\"  onclick=\"pickElem('O');\">O</td>";
  html += "<td class=\"main\" id=\"mF\"  onclick=\"pickElem('F');\">F</td>";
  html += "<td class=\"metl\" id=\"pNe\" onclick=\"pickElem('Ne');\">Ne</td>";
  html += "</tr>\n";

  html += "<tr>";
  html += "<td class=\"metl\" id=\"pNa\" onclick=\"pickElem('Na');\">Na</td>";
  html += "<td class=\"metl\" id=\"pMg\" onclick=\"pickElem('Mg');\">Mg</td>";
  html += "<td class=\"Row\"  id=\"Row3\" colspan=\"10\">&nbsp;</td>";
  html += "<td class=\"main\" id=\"mAl\" onclick=\"pickElem('Al')\">Al</td>";
  html += "<td class=\"main\" id=\"mSi\" onclick=\"pickElem('Si')\">Si</td>";
  html += "<td class=\"main\" id=\"mP\"  onclick=\"pickElem('P')\">P</td>";
  html += "<td class=\"main\" id=\"mS\"  onclick=\"pickElem('S')\">S</td>";
  html += "<td class=\"main\" id=\"mCl\" onclick=\"pickElem('Cl')\">Cl</td>";
  html += "<td class=\"metl\" id=\"pAr\" onclick=\"pickElem('Ar')\">Ar</td>";
  html += "</tr>\n";

  html += "<tr>";
  html += "<td class=\"metl\" id=\"pK\"  onclick=\"pickElem('K')\">K</td>";
  html += "<td class=\"metl\" id=\"pCa\" onclick=\"pickElem('Ca')\">Ca</td>";
  html += "<td class=\"metl\" id=\"pSc\" onclick=\"pickElem('Sc')\">Sc</td>";
  html += "<td class=\"metl\" id=\"pTi\" onclick=\"pickElem('Ti')\">Ti</td>";
  html += "<td class=\"metl\" id=\"pV\"  onclick=\"pickElem('V')\">V</td>";
  html += "<td class=\"metl\" id=\"pCr\" onclick=\"pickElem('Cr')\">Cr</td>";
  html += "<td class=\"metl\" id=\"pMn\" onclick=\"pickElem('Mn')\">Mn</td>";
  html += "<td class=\"metl\" id=\"pFe\" onclick=\"pickElem('Fe')\">Fe</td>";
  html += "<td class=\"metl\" id=\"pCo\" onclick=\"pickElem('Co')\">Co</td>";
  html += "<td class=\"metl\" id=\"pNi\" onclick=\"pickElem('Ni')\">Ni</td>";
  html += "<td class=\"metl\" id=\"pCu\" onclick=\"pickElem('Cu')\">Cu</td>";
  html += "<td class=\"metl\" id=\"pZn\" onclick=\"pickElem('Zn')\">Zn</td>";
  html += "<td class=\"main\" id=\"mGa\" onclick=\"pickElem('Ga')\">Ga</td>";
  html += "<td class=\"main\" id=\"mGe\" onclick=\"pickElem('Ge')\">Ge</td>";
  html += "<td class=\"main\" id=\"mAs\" onclick=\"pickElem('As')\">As</td>";
  html += "<td class=\"main\" id=\"mSe\" onclick=\"pickElem('Se')\">Se</td>";
  html += "<td class=\"main\" id=\"mBr\" onclick=\"pickElem('Br')\">Br</td>";
  html += "<td class=\"metl\" id=\"pKr\" onclick=\"pickElem('Kr')\">Kr</td>";
  html += "</tr>\n";

  html += "<tr>";
  html += "<td class=\"metl\" id=\"pRb\" onclick=\"pickElem('Rb')\">Rb</td>";
  html += "<td class=\"metl\" id=\"pSr\" onclick=\"pickElem('Sr')\">Sr</td>";
  html += "<td class=\"metl\" id=\"pY\"  onclick=\"pickElem('Y')\">Y</td>";
  html += "<td class=\"metl\" id=\"pZr\" onclick=\"pickElem('Zr')\">Zr</td>";
  html += "<td class=\"metl\" id=\"pNb\" onclick=\"pickElem('Nb')\">Nb</td>";
  html += "<td class=\"metl\" id=\"pMo\" onclick=\"pickElem('Mo')\">Mo</td>";
  html += "<td class=\"metl\" id=\"pTc\" onclick=\"pickElem('Tc')\">Tc</td>";
  html += "<td class=\"metl\" id=\"pRu\" onclick=\"pickElem('Ru')\">Ru</td>";
  html += "<td class=\"metl\" id=\"pRh\" onclick=\"pickElem('Rh')\">Rh</td>";
  html += "<td class=\"metl\" id=\"pPd\" onclick=\"pickElem('Pd')\">Pd</td>";
  html += "<td class=\"metl\" id=\"pAg\" onclick=\"pickElem('Ag')\">Ag</td>";
  html += "<td class=\"metl\" id=\"pCd\" onclick=\"pickElem('Cd')\">Cd</td>";
  html += "<td class=\"main\" id=\"mIn\" onclick=\"pickElem('In')\">In</td>";
  html += "<td class=\"main\" id=\"mSn\" onclick=\"pickElem('Sn')\">Sn</td>";
  html += "<td class=\"main\" id=\"mSb\" onclick=\"pickElem('Sb')\">Sb</td>";
  html += "<td class=\"main\" id=\"mTe\" onclick=\"pickElem('Te')\">Te</td>";
  html += "<td class=\"main\" id=\"mI\"  onclick=\"pickElem('I')\">I</td>";
  html += "<td class=\"metl\" id=\"pXe\" onclick=\"pickElem('Xe')\">Xe</td>";
  html += "</tr>\n";

  html += "<tr>";
  html += "<td class=\"metl\" id=\"pCs\" onclick=\"pickElem('Cs')\">Cs</td>";
  html += "<td class=\"metl\" id=\"pBa\" onclick=\"pickElem('Ba')\">Ba</td>";
  html += "<td class=\"metl\" id=\"pLa\" onclick=\"pickElem('La')\">La</td>";
  html += "<td class=\"metl\" id=\"pHf\" onclick=\"pickElem('Hf')\">Hf</td>";
  html += "<td class=\"metl\" id=\"pTa\" onclick=\"pickElem('Ta')\">Ta</td>";
  html += "<td class=\"metl\" id=\"pW\"  onclick=\"pickElem('W')\">W</td>";
  html += "<td class=\"metl\" id=\"pRe\" onclick=\"pickElem('Re')\">Re</td>";
  html += "<td class=\"metl\" id=\"pOs\" onclick=\"pickElem('Os')\">Os</td>";
  html += "<td class=\"metl\" id=\"pIr\" onclick=\"pickElem('Ir')\">Ir</td>";
  html += "<td class=\"metl\" id=\"pPt\" onclick=\"pickElem('Pt')\">Pt</td>";
  html += "<td class=\"metl\" id=\"pAu\" onclick=\"pickElem('Au')\">Au</td>";
  html += "<td class=\"metl\" id=\"pHg\" onclick=\"pickElem('Hg')\">Hg</td>";
  html += "<td class=\"main\" id=\"mTl\" onclick=\"pickElem('Tl')\">Tl</td>";
  html += "<td class=\"main\" id=\"mPb\" onclick=\"pickElem('Pb')\">Pb</td>";
  html += "<td class=\"main\" id=\"mBi\" onclick=\"pickElem('Bi')\">Bi</td>";
  html += "<td class=\"main\" id=\"mPo\" onclick=\"pickElem('Po')\">Po</td>";
  html += "<td class=\"main\" id=\"mAt\" onclick=\"pickElem('At')\">At</td>";
  html += "<td class=\"metl\" id=\"pRn\" onclick=\"pickElem('Rn')\">Rn</td>";
  html += "</tr>\n";

  html += "<tr>";
  html += "<td class=\"metl\" id=\"pFr\"  onclick=\"pickElem('Fr')\">Fr</td>";
  html += "<td class=\"metl\" id=\"pRa\"  onclick=\"pickElem('Ra')\">Ra</td>";
  html += "<td class=\"metl\" id=\"pAc\"  onclick=\"pickElem('Ac')\">Ac</td>";
  html += "<td class=\"metl\" id=\"pRf\"  onclick=\"pickElem('Rf')\">Rf</td>";
  html += "<td class=\"metl\" id=\"pDb\"  onclick=\"pickElem('Db')\">Db</td>";
  html += "<td class=\"metl\" id=\"pSg\"  onclick=\"pickElem('Sg')\">Sg</td>";
  html += "<td class=\"metl\" id=\"pBh\"  onclick=\"pickElem('Bh')\">Bh</td>";
  html += "<td class=\"metl\" id=\"pHs\"  onclick=\"pickElem('Hs')\">Hs</td>";
  html += "<td class=\"metl\" id=\"pMt\"  onclick=\"pickElem('Mt')\">Mt</td>";
  html += "<td class=\"metl\" id=\"pDs\"  onclick=\"pickElem('Ds')\">Ds</td>";
  html += "<td class=\"metl\" id=\"pRg\"  onclick=\"pickElem('Rg')\">Rg</td>";
  html += "<td class=\"metl\" id=\"pCn\"  onclick=\"pickElem('Cn')\">Cn</td>";
  html += "<td class=\"metl\" id=\"pUut\" onclick=\"pickElem('Uut')\">Uut</td>";
  html += "<td class=\"metl\" id=\"pFl\"  onclick=\"pickElem('Fl')\">Fl</td>";
  html += "<td class=\"metl\" id=\"pUup\" onclick=\"pickElem('Uup')\">Uup</td>";
  html += "<td class=\"metl\" id=\"pLv\"  onclick=\"pickElem('Lv')\">Lv</td>";
  html += "<td class=\"metl\" id=\"pUus\" onclick=\"pickElem('Uus')\">Uus</td>";
  html += "<td class=\"metl\" id=\"pUuo\" onclick=\"pickElem('Uuo')\">Uuo</td>";
  html += "</tr>\n";

  html += "<tr>";
  html += "<td class=\"Row\"  id=\"RowLa\" colspan=\"2\">&nbsp;</td>";
  html += "<td class=\"metl\" id=\"pCe\" onclick=\"pickElem('Ce')\">Ce</td>";
  html += "<td class=\"metl\" id=\"pPr\" onclick=\"pickElem('Pr')\">Pr</td>";
  html += "<td class=\"metl\" id=\"pNd\" onclick=\"pickElem('Nd')\">Nd</td>";
  html += "<td class=\"metl\" id=\"pPm\" onclick=\"pickElem('Pm')\">Pm</td>";
  html += "<td class=\"metl\" id=\"pSm\" onclick=\"pickElem('Sm')\">Sm</td>";
  html += "<td class=\"metl\" id=\"pEu\" onclick=\"pickElem('Eu')\">Eu</td>";
  html += "<td class=\"metl\" id=\"pGd\" onclick=\"pickElem('Gd')\">Gd</td>";
  html += "<td class=\"metl\" id=\"pTb\" onclick=\"pickElem('Tb')\">Tb</td>";
  html += "<td class=\"metl\" id=\"pDy\" onclick=\"pickElem('Dy')\">Dy</td>";
  html += "<td class=\"metl\" id=\"pHo\" onclick=\"pickElem('Ho')\">Ho</td>";
  html += "<td class=\"metl\" id=\"pEr\" onclick=\"pickElem('Er')\">Er</td>";
  html += "<td class=\"metl\" id=\"pTm\" onclick=\"pickElem('Tm')\">Tm</td>";
  html += "<td class=\"metl\" id=\"pYb\" onclick=\"pickElem('Yb')\">Yb</td>";
  html += "<td class=\"metl\" id=\"pLu\" onclick=\"pickElem('Lu')\">Lu</td>";
  html += "<td class=\"Row\"  id=\"RowLa2\" colspan=\"2\">&nbsp;</td>";
  html += "</tr>\n";

  html += "<tr>";
  html += "<td class=\"Row\"  id=\"RowAc\" colspan=\"2\">&nbsp;</td>";
  html += "<td class=\"metl\" id=\"pTh\" onclick=\"pickElem('Th')\">Th</td>";
  html += "<td class=\"metl\" id=\"pPa\" onclick=\"pickElem('Pa')\">Pa</td>";
  html += "<td class=\"metl\" id=\"pU\"  onclick=\"pickElem('U')\" >U</td>";
  html += "<td class=\"metl\" id=\"pNp\" onclick=\"pickElem('Np')\">Np</td>";
  html += "<td class=\"metl\" id=\"pPu\" onclick=\"pickElem('Pu')\">Pu</td>";
  html += "<td class=\"metl\" id=\"pAm\" onclick=\"pickElem('Am')\">Am</td>";
  html += "<td class=\"metl\" id=\"pCm\" onclick=\"pickElem('Cm')\">Cm</td>";
  html += "<td class=\"metl\" id=\"pBk\" onclick=\"pickElem('Bk')\">Bk</td>";
  html += "<td class=\"metl\" id=\"pCf\" onclick=\"pickElem('Cf')\">Cf</td>";
  html += "<td class=\"metl\" id=\"pEs\" onclick=\"pickElem('Es')\">Es</td>";
  html += "<td class=\"metl\" id=\"pFm\" onclick=\"pickElem('Fm')\">Fm</td>";
  html += "<td class=\"metl\" id=\"pMd\" onclick=\"pickElem('Md')\">Md</td>";
  html += "<td class=\"metl\" id=\"pNo\" onclick=\"pickElem('No')\">No</td>";
  html += "<td class=\"metl\" id=\"pLr\" onclick=\"pickElem('Lr')\">Lr</td>";
  html += "<td class=\"Row\"  id=\"RowAc2\" colspan=\"2\">&nbsp;</td>";
  html += "</tr></table>\n";

  // Write html code to division
  var divID = document.getElementById(PerDivision);
  if ( divID ) {
    divID.innerHTML = html;
    }

  // End of drawPeriodic routine
  }
//
// -------------------- molecule.js --------------------
//

//#   function Mol(value)
//#
//#   Define public routine to store and return molecule arrays
//#
//#   Parameter:
//#     value = If value given, then set as active molecule
//# 
//#   Return value:
//#     Pointer to current array for molecular coordinates, ex.
//#        var molecule = Mol();
//#
//#   Molecular values stored in 'zeroth' element of array
//#     molecule[0].molIndex    - ID number for this molecule
//#     molecule[0].numatoms    - # of atoms in this molecule 
//#     molecule[0].AtomScale   - Scale factor to control size of molecule displayed
//#     molecule[0].showlabels  - 0=don't show elemental symbols, 1=show symbols
//#     molecule[0].showcharges - 0=don't show charges, 1=show charges
//#     molecule[0].gradients   - 0=don't shade atoms, 1=use shading
//#     molecule[0].formula     - Simple text string containing molecular formula
//#     molecule[0].weight      - Molecular weight
//#     molecule[0].charge      - Charge of molecule
//#
//#   Atomic values in remaining elements of array
//#     molecule[i].atomicnumber - Atomic number (Z) for atom
//#     molecule[i].x            - x coordinate of atom
//#     molecule[i].y            - y coordinate of atom
//#     molecule[i].z            - z coordinate of atom
//#     molecule[i].charge       - Estimate of atomic charge
//#     molecule[i].highlite     - 0=don't highlight atom, 1=highlight atom
//#     molecule[i].hide         - 0=display atom, 1=do not display atom
//#
function Mol(value) {
  // Declare local variables
  var id;
  var param = value || 0;

  // Determine which molecule to use
  if(typeof Mol.molecule === "undefined")
    Mol.molecule = 1;
  if ( param > 0 ) {
    Mol.molecule = param;
    BondMatrix(param);
    }
  id = Mol.molecule;

  // Initialize molecular array if necessary
  if ( typeof Mol.moly === "undefined" )
    Mol.moly = [];
  if ( typeof Mol.moly[id] === "undefined" ) {
    Mol.moly[id] = [];
    Mol.moly[id][0] = new molObject();
    Mol.moly[id][0].molIndex = id;
    Mol.moly[id][0].numatoms = 0;
    Mol.moly[id][0].AtomScale = 1;
    Mol.moly[id][0].showlabels = 0;
    Mol.moly[id][0].showcharges = 0;
    Mol.moly[id][0].gradients = 1;
    Mol.moly[id][0].highlite = 0;
    Mol.moly[id][0].formula = "";
    Mol.moly[id][0].weight = 0.0;
    Mol.moly[id][0].charge = 999;
    }

  // End of Mol routine
  return Mol.moly[id];
  }


//#   function BondMatrix(value)
//#
//#   Define public routine to store and return Bond Matrix
//#
//#   Parameter:
//#      value = If value given, then set as active matrix
//# 
//#   Return value:
//#      Pointer to current bond matrix, ex.
//#        var bonds = BondMatrix();
//#        bonds[i][j] then gives indication of bond between atoms "i" and "j"
//#
function BondMatrix(value) {
  // Declare local variables
  var id;
  var param = value || 0;

  // Determine which bond matrix to use
  if(typeof BondMatrix.id === "undefined")
    BondMatrix.id = 1;
  if ( param > 0 )
    BondMatrix.id = param;
  id = BondMatrix.id;

  // Initialize molecular array if necessary
  if ( typeof BondMatrix.bonds === "undefined" )
    BondMatrix.bonds = [];
  if ( typeof BondMatrix.bonds[id] === "undefined" ) {
    BondMatrix.bonds[id] = [];
    }

  // End of BondMatrix routine
  return BondMatrix.bonds[id];
  }


///
///  Private routine to store name for active window.
///
///  Parameter:
///    mywin = If name of window exists, then set as active window/molecule.
///            Otherwise, create new window with this name.
/// 
///  Return value:
///    Name of active Canvas/window
///
function activeWin(mywin) {

  // Declare local variables
  var i, active;
  var param = mywin || " ";

  // Initialize links
  if (typeof activeWin.mol === "undefined") {
    activeWin.mol = [];
    activeWin.mol[0] = "Dummy";
    }

  // Define defaults for active window and molecule
  if (typeof activeWin.win === "undefined") {
    var tag = document.getElementsByTagName("canvas");
    if ( tag[0] ) {
        activeWin.win = tag[0].id;
        activeWin.mol[1] = activeWin.win;
      } else {
        // alert("No canvas element found.");
        return;
      }
    }

  // User requested to set/view Window information
  if ( param.length > 1 )
    activeWin.win = param;

  // Find active molecule
  active=-1;
  for (i=0; i<activeWin.mol.length; i++)
    if ( activeWin.mol[i] == activeWin.win )
      active = i;

  // If requested window not found, add to list
  if ( active < 0 ) {
    active = activeWin.mol.length;
    activeWin.mol[active] = activeWin.win;
    }

  // Make correct molecule active
  Mol(active);

  // Define routines used to handle mouse events
  var canvas = document.getElementById(activeWin.win);
  if ( canvas ) {
    canvas.onmousedown = MouseDown;
    document.onmouseup = MouseUp;
    canvas.onmousemove = MouseMove;
    canvas.addEventListener("mousewheel", MouseWheel, false);  // IE9,Chrome,Safari,Opera
    canvas.addEventListener("DOMMouseScroll", MouseWheel, false); // Firefox
    canvas.addEventListener("touchstart", MouseDown);
    canvas.addEventListener("touchend", MouseUp);
    canvas.addEventListener("touchmove", MouseMove);
    }

  // Finished with activeWin routine
  return activeWin.win;
  }


///
/// Define structure for each atom
///
function atomObject() {
  this.atomicnumber = 0;
  this.x = 0.0;
  this.y = 0.0;
  this.z = 0.0;
  this.charge = 0.0;
  this.highlite = 0;
  }


///
/// Define structure for molecular information
///
function molObject() {
  this.molIndex = 1;
  this.numatoms = 0;
  this.AtomScale = 1.0;
  this.showlabels = 1;
  this.showcharges = 0;
  this.gradients = 1;
  this.highlite = 0;
  this.hide = 0;
  this.formula = "";
  this.weight = 0.0;
  this.charge = 999;
  }


///   function readXYZfile(lines)
///
///   Read xyz file - Format compatible with openbabel
///
///   lines:    Array holding content of .xyz file as lines
///
///   Data stored in molecule array and bond matrix
///
function readXYZfile(lines) {
  // Declare local variables
  var i, j, numatoms;
  var A, x, y, z;
  var dx, dy, dz, r;
  var bond;
  var mystr;
  var current = new Array();
  var Qtitle = new Array();
  var molecule = Mol();
  // Reset molecule object and contents
  delMolecule();

  // Read data
  InfoWin("",1);
  numatoms = parseInt(lines[0].replace(/\s+/,""));
  if ( isNaN(numatoms) ) {
    InfoWin("*** ERROR Reading XYZ file. ***\n");
    return;
    }
  Qtitle = lines[1];
  Qtitle = Qtitle.replace(/\s+$/,"");
  InfoWin(Qtitle+"\n");
  InfoWin("Looking for "+numatoms+" atoms.\n");

  // Read coordinates
  for (i=2; i < (numatoms+2); i++) {
    current = lines[i].replace(/\s+/g," ").replace(/^\s+/,"").split(' ');
    A = lookupSymbol(current[0]);
    //console.log(A, current[0])
    if ( (A<1) || (A>118) ) {
      InfoWin("*** ERROR Reading XYZ file. ***\n");
      return;
      }
    x = parseFloat(current[1]);
    y = parseFloat(current[2]);
    z = parseFloat(current[3]);
    addAtom(A, x, y, z);
    InfoWin(" "+current[0]+"("+A+")  "+x+", "+y+", "+z+"\n");
    }

  // Create bonds
  for (i=1; i < numatoms; i++) {
    for (j=i+1; j <= numatoms; j++) {
      bond = 1.2 * (element(molecule[i].atomicnumber,"radius") + element(molecule[j].atomicnumber,"radius"));
      dx = molecule[i].x - molecule[j].x;
      dy = molecule[i].y - molecule[j].y;
      dz = molecule[i].z - molecule[j].z;
      r = Math.sqrt(dx*dx+dy*dy+dz*dz);
      //console.log(molecule[i])
      if (r <= bond)
        addBond(i,j);
      }
    }

  // Finished with readXYZfile routine
  formula();
  InfoWin("Finished reading XYZ input file.\n");
  }
///   function readMOLfile(molfile,lines)
///
///   Read MDL .mol file (V2000 format)
///
///   molfile:  name of .mol file
///   lines:    Array holding content of .mol file
///
///   Data stored in molecule array and bond matrix
///

//#   function lookupSymbol(symbol)
//#
//#   Given elemental symbol, lookup and return atomic number (Z)
//#
function readMOLfile(molfile,lines) {
  // Declare local variables
  var i, j;
  var x, y, z;
  var bond1, bond2;
  var A, symbol;
  var Qtitle = new Array();
  var molecule = Mol();
  // Write file information to information window
  var molname = escape(molfile.name);
  InfoWin("File Name = "+molname,1);
  InfoWin("\nFile Type = "+molfile.type);
  InfoWin("\nFile Size = "+molfile.size);

  // Reset molecule object and contents
  delMolecule();

  // Read data
  Qtitle = lines[0];
  Qtitle = Qtitle.replace(/\s+$/,"");
  var molAtoms = parseFloat(lines[3].substr(0,3));
  var molBonds = parseFloat(lines[3].substr(3,3));
  InfoWin("\n\n"+Qtitle);
  InfoWin("\n"+molAtoms+" atoms and "+molBonds+" bonds.");

  // Read coordinates
  j = molAtoms+4;
  for (i=4; i < j; i++) {
    x = parseFloat(lines[i].substr(0,10));
    y = parseFloat(lines[i].substr(10,10));
    z = parseFloat(lines[i].substr(20,10));
    symbol = lines[i].substr(31,3);
    symbol = symbol.replace(/\s+/,"");
    A = lookupSymbol(symbol);
    InfoWin("\n   "+symbol+"("+A+")  "+x+", "+y+", "+z);
    addAtom(A, x, y, z);
    }
  j = 4 + molAtoms + molBonds;
  for (i = 4+molAtoms; i < j; i++) {
    bond1 = parseFloat(lines[i].substr(0,3));
    bond2 = parseFloat(lines[i].substr(3,3));
    InfoWin("\n   Bond from "+bond1+" to "+bond2);
    addBond(bond1,bond2);
    }
  // Finished
  formula();
  } 


///
///   Read GAMESS input file contain full set of x,y,z coordinates
///
///   lines:    Array holding content of .inp file
///
function readINPfile(lines) {
  // Declare local variables
  var i, j;
  var x, y, z;
  var bond1, bond2;
  var A, symbol;
  var numatoms;
  var Qtitle = new Array();
  var molecule = Mol();

  // Inform user that file being read
  InfoWin("--- Reading Gamess input file ---\n",1);

  // Reset molecule object and contents
  delMolecule();

  // Read title from file
  i = 0;
  lines[i].toLowerCase();
  while ( lines[i].toLowerCase().indexOf('$data') < 0 ) {
    i++;
    }
  i++;
  Qtitle = lines[i];
  Qtitle = Qtitle.replace(/\s+$/,"");
  InfoWin("\n\nTitle: [" + Qtitle + "]\n");

  // Advance to start of coordinates
  i++;
  if ( lines[i].toLowerCase().indexOf('c1') < 0 )
    i++;

  // Read coordinates
  i++;
  while ( lines[i].toLowerCase().indexOf('$end') < 0 ) {
    InfoWin("   Line = [" + lines[i] + "]\n");
    current = lines[i].replace(/\s+/g," ").replace(/^\s+/,"").split(' ');
    A = parseInt(current[1]);
    x = parseFloat(current[2]);
    y = parseFloat(current[3]);
    z = parseFloat(current[4]);
    addAtom(A, x, y, z);
    i++;
    }

  // Calculate bonds
  for (i=1; i < molecule[0].numatoms; i++) {
    ra = element(molecule[i].atomicnumber,"radius");
    for (j=i+1; j <= molecule[0].numatoms; j++) {
      rb = element(molecule[i].atomicnumber,"radius");
      r = 0.9*distance(molecule, i, j);
      if ( r <= (ra+rb) )
        addBond(i, j);
      }
    }

  // Finished with readINPfile routine
  InfoWin("Finished reading input file.\n");
  formula();
  return;
  }


function readCIFfile(molfile, lines) {
  // Declare local variables
  var i, j, numatoms, cosstar, xcor, ycor, zcor;
  var Atm, x, y, z, a, b, c, alpha, beta, gamma;
  var dx, dy, dz, r;
  var bond;
  var mystr;
  var atomindex, loopindex;
  var atomxyz = new Array();
  //var current = new Array();
 // var Qtitle = new Array();
  var molecule = Mol();
  // Reset molecule object and contents
  delMolecule();
  var patt = new RegExp(/([A-Za-z]{1,2}[0-9]{0,2}[\w]{0,}[\s]*[\w]{0,2}[\s]+([+-]?([0-9]*[.])?[0-9]+[/(]?[0-9]*?[/)]?[\s]){3,7}(.*?)*)/);
  // Read data
  InfoWin("",1);
  var cycle;

  for (i=0; i < (lines.length); i++) {

     if ((lines[i].trim()).startsWith("_atom_site_label")){
        atomindex = i;
        }
     if ((lines[i].trim()).startsWith("loop_")){
        if (typeof atomindex !== 'undefined') {
           if (atomindex < i){
               if (typeof cycle == 'undefined') {
                  loopindex = i;

                  cycle=1;
              }
           }
        }
     }

     if (lines[i].startsWith("_cell_length_a")){
        a = parseFloat(lines[i].replace("_cell_length_a",""));
//        console.log(lines[i])
     }
     if (lines[i].startsWith("_cell_length_b")){
        b = parseFloat(lines[i].replace("_cell_length_b",""));

     }
     if (lines[i].startsWith("_cell_length_c")){
        c = parseFloat(lines[i].replace("_cell_length_c",""));

     }
     if (lines[i].startsWith("_cell_angle_alpha")){
        alpha = parseFloat(lines[i].replace("_cell_angle_alpha",""));

     }
     if (lines[i].startsWith("_cell_angle_beta")){
        beta = parseFloat(lines[i].replace("_cell_angle_beta",""));
     }
     if (lines[i].startsWith("_cell_angle_gamma")){
        gamma = parseFloat(lines[i].replace("_cell_angle_gamma",""));

     }
     if (typeof atomindex !== 'undefined') {
         if (typeof loopindex == 'undefined') {
            //console.log(atomindex, loopindex);
//            console.log(i);
            if (i >= atomindex) {
//              console.log("atomi", atomindex);
              if (patt.test(lines[i]+"\n")){
//                console.log("patt", lines[i]);
                mystr = lines[i].split(/\s+/);

                if (isNaN(mystr[1][0])){
                   Atm = lookupSymbol(mystr[1].replace(/\s+/g," ").replace(/^\s+/,"").split(' '));
                   x = parseFloat(mystr[2]);
                   y = parseFloat(mystr[3]);
                   z = parseFloat(mystr[4]);
                   //console.log(Atm, mystr);
                   }
                else {

                   Atm = lookupSymbol(((mystr[0]).split(/[0-9]+/))[0]);
                   x = parseFloat(mystr[1]);
                   y = parseFloat(mystr[2]);
                   z = parseFloat(mystr[3]);
                   //console.log(Atm, mystr);
                  }

        cosstar=((Math.cos(beta* Math.PI / 180) * Math.cos(gamma * Math.PI / 180)-Math.cos(alpha * Math.PI / 180))/(Math.sin(gamma * Math.PI / 180) * Math.sin(beta * Math.PI / 180)));
        xcor=a * x + (b * Math.cos(gamma* Math.PI / 180)) * y + c*Math.cos(beta * Math.PI / 180) * z * Math.sin(beta * Math.PI / 180);
        ycor=(b * Math.sin(gamma * Math.PI / 180)) * y - c * cosstar * z;
        zcor=(c * Math.sin(beta * Math.PI / 180)) * z * Math.sqrt(1 - (Math.cos(alpha * Math.PI / 180)) * (Math.cos(alpha * Math.PI / 180)));
        addAtom(Atm, xcor, ycor, zcor);
        //atomxyz=[[Atm, xcor, ycor, zcor]]
        InfoWin(" "+mystr[1]+"("+Atm+")  "+xcor+", "+ycor+", "+zcor+"\n");
     }else {
         console.log("no",lines[i]);
     }
  }
  }
  }
  }

   for (i=1; i < (molecule.length-1); i++) {
    for (j=i+1; j < (molecule.length-1); j++) {
      bond = 1.2 * (element(molecule[i].atomicnumber,"radius") + element(molecule[j].atomicnumber,"radius"));
      dx = molecule[i].x - molecule[j].x;
      dy = molecule[i].y - molecule[j].y;
      dz = molecule[i].z - molecule[j].z;
      r = Math.sqrt(dx*dx+dy*dy+dz*dz);
      if (r <= bond)
        addBond(i,j);
      }
    }
  formula();
  return;


  }

function readRESfile(molfile, lines) {
  // Declare local variables
  var i, j, numatoms, cosstar, xcor, ycor, zcor;
  var Atm, x, y, z, a, b, c, alpha, beta, gamma, label;
  var dx, dy, dz, r;
  var bond;
  var mystr;
  var atomindex, loopindex;
  var atomxyz = new Array();
  console.log("reading res file");
  var molecule = Mol();
  // Reset molecule object and contents
  delMolecule();
  //[A-Za-z]{1,2}[0-9]{0,2}[\w]{0,}[\s]*[\w]{0,2}[\s]+([+-]?([0-9]*[.])?[0-9]+[/(]?[0-9]*?[/)]?[\s]){3,4}(.*?)*
  //[A-Za-z]{1,2}[0-9]{0,2}[\w]{0,}[\s]+[\w]{0,2}[\s]+([+-]?([0-9]*[.])?[0-9]+[/(]?[0-9]*?[/)]?[\s]){4}(.*?)*)*
  var patt = new RegExp(/([A-Za-z]{1,2}[0-9]{0,2}[\w]{0,}[\s]*[\d]{1,3}[\s]+([+-]?([0-9]*[.])?[0-9]{0,6}[\s]){2,})/);
  //  var patt = new RegExp(/([A-Za-z]{1,2}[0-9]{0,2}[\w]{0,}[\s]*[\w]{0,2}[\s]+([+-]?([0-9]*[.])?[0-9]+[/(]?[0-9]*?[/)]?[\s]){3,4}(.*?)*)/);
  // Read data
  InfoWin("",1);

  for (i=0; i < (lines.length); i++) {
     if (lines[i].startsWith("CELL")){
        var cell = (lines[i].replace("CELL","")).split(' ').map(Number).filter(Boolean);
        a = parseFloat(cell[1]);
        b = parseFloat(cell[2]);
        c = parseFloat(cell[3]);
        alpha = parseFloat(cell[4]);
        beta =parseFloat(cell[5]);
        gamma = parseFloat(cell[6]);
     }

     if (patt.test(lines[i])){
        mystr = lines[i].split(/\s+/);
        if  (["ZERR","OMIT","UNIT", "HKLF", "PART", "RESI"].indexOf(mystr[0].toUpperCase()) < 0){ // need upper
        if (mystr[0][0]!=="Q"){
           label = mystr[0] 
           var atml = (label).split(/[0-9]+/)[0];
           if (atml.length==1){
              Atm = lookupSymbol(atml);
              }else {
              atml = atml.split('');
              atml[1]=atml[1].toLowerCase();
              atml = atml.join('');
              Atm = lookupSymbol(atml);
              }
           x = parseFloat(mystr[2]);
           y = parseFloat(mystr[3]);
           z = parseFloat(mystr[4]);
//           console.log((mystr[0]), Atm, atml);
//           console.log(x, y, z, a, b, c, alpha, beta, gamma);
        cosstar=((Math.cos(beta* Math.PI / 180) * Math.cos(gamma * Math.PI / 180)-Math.cos(alpha * Math.PI / 180))/(Math.sin(gamma * Math.PI / 180) * Math.sin(beta * Math.PI / 180)));
        xcor=a * x + (b * Math.cos(gamma* Math.PI / 180)) * y + c*Math.cos(beta * Math.PI / 180) * z * Math.sin(beta * Math.PI / 180);
        ycor=(b * Math.sin(gamma * Math.PI / 180)) * y - c * cosstar * z;
        zcor=(c * Math.sin(beta * Math.PI / 180)) * z * Math.sqrt(1 - (Math.cos(alpha * Math.PI / 180)) * (Math.cos(alpha * Math.PI / 180)));
        addAtom(Atm, xcor, ycor, zcor, atomLabel, label);
        // console.log(mystr, Atm, xcor, ycor, zcor);
        InfoWin(" "+mystr[1]+"("+Atm+")  "+xcor+", "+ycor+", "+zcor+"\n");
         }
         }
     }
  }
   for (i=1; i <= (molecule.length-1); i++) {
    for (j=i+1; j <= (molecule.length-1); j++) {
      bond = 1.3 * (element(molecule[i].atomicnumber,"radius") + element(molecule[j].atomicnumber,"radius"));
      dx = molecule[i].x - molecule[j].x;
      dy = molecule[i].y - molecule[j].y;
      dz = molecule[i].z - molecule[j].z;
      r = Math.sqrt(dx*dx+dy*dy+dz*dz);
      //console.log(molecule[i], r);
      if (r <= bond)
        addBond(i,j);
      }
    }
  formula();
  return;


  }

function readPDBfile(molfile, pdb_string) {
    var molecule = Mol();
    // Reset molecule object and contents
    delMolecule();
    var lines = pdb_string;
    for (var i = 0; i < lines.length; i++) {
      var line = lines[i].split(/\s+/);
      if (line[0] == "ATOM" || line[0] == "HETATM" ) {

        // console.log(line, x, y, z);
        var name = lines[i].substring(12,16).trim()[0];
        var altloc = lines[i].substring(16, 17).trim();
        var resname = lines[i].substring(17, 20).trim();
        var chain = lines[i].substring(20, 22).trim();
        var resseq = lines[i].substring(22, 26);
        var _resseq_as_int = null;
        var icode = lines[i].substring(26, 27).trim();
        var x = parseFloat(lines[i].substring(30, 38));
        var y = parseFloat(lines[i].substring(38, 46));
        var z = parseFloat(lines[i].substring(46, 54));
        //console.log(name,  x, y, z);
        atml = line[2].replace(/[^A-Za-z]+/g, '');
        Atm = lookupSymbol(atml);
        addAtom(Atm, x, y, z);
    }
  
  }
  for (i=1; i <= (molecule.length-1); i++) {
    for (j=i+1; j <= (molecule.length-1); j++) {
      bond = 1.3 * (element(molecule[i].atomicnumber,"radius") + element(molecule[j].atomicnumber,"radius"));
      dx = molecule[i].x - molecule[j].x;
      dy = molecule[i].y - molecule[j].y;
      dz = molecule[i].z - molecule[j].z;
      r = Math.sqrt(dx*dx+dy*dy+dz*dz);
      //console.log(molecule[i], r);
      if (r <= bond)
        addBond(i,j);
      }
    }
  formula();
  return;
}


function lookupSymbol(symbol) {
  var i;

  for (i = 1; i < element(1,"max"); i++) {
    if ( element(i,"symbol") == symbol )
      return i;
    }
  return 0;
  }


///
///   Routine to remove and initialize molecule object
///
function delMolecule() {
  var molecule = Mol();

  molecule[0] = new molObject();
  molecule[0].molIndex = 1;
  molecule[0].numatoms = 0;
  molecule[0].AtomScale = 1.0;
  molecule[0].showlabels = 0;
  molecule[0].showcharges = 0;
  buttonColor("ChargeButton",0);
  }


///
///  Routine to save/restore molecular coordinates, bonds, ...
///
///  Parameter: mode
///      pop  - restore last saved set of coordinates
///      save - store current information
///      redo - 'Undo' last pop
///
function Undo(mode) {

  // Declare local variables
  var i, pos;
  var maxBonds;
  var MAXSAVE=10;
  var molecule = Mol();
  var bonds = BondMatrix();

  // Initialization of variables
  if ( typeof Undo.num == 'undefined' ) {
    Undo.num = 0;
  	Undo.mol = [];
  	Undo.bonds = [];
  	for (i=0; i < MAXSAVE; i++) {
  	  Undo.mol[i] = [];
  	  Undo.mol[i][0] = 0;
  	  Undo.bonds[i] = [];
  	  }
    }

  // Save current geometry information
  if ( mode == "save")  {
  	pos = Undo.num;
    // InfoWin(" --- Saving geometry in slot " + pos + " ---\n");
  	Undo.mol[pos] = null;
  	Undo.mol[pos] = [];
    Undo.mol[pos][0] = molecule[0].numatoms;
    for (i=1; i <= molecule[0].numatoms; i++) {
      Undo.mol[pos][i] = new atomObject();
      Undo.mol[pos][i].atomicnumber = molecule[i].atomicnumber;
      Undo.mol[pos][i].x = molecule[i].x;
      Undo.mol[pos][i].y = molecule[i].y;
      Undo.mol[pos][i].z = molecule[i].z;
      Undo.mol[pos][i].bonds = [];
      Undo.mol[pos][i].charge = molecule[i].charge;
      Undo.mol[pos][i].highlite = molecule[i].highlite;
      }
  	Undo.bonds[pos] = null;
  	Undo.bonds[pos] = [];
    for (i=1; i <= molecule[0].numatoms; i++) {
      Undo.bonds[pos][i] = [];
      for (j=0; j <= molecule[0].numatoms; j++) {
        Undo.bonds[pos][i][j] = bonds[i][j];
        }
      }

    // alert("Coordinate set "+Undo.num+" contains "+Undo.mol[pos][0]+" atoms.");
    Undo.num = ( (Undo.num+1) % MAXSAVE );
    return;
    }

  // Set position of 'last saved' geometry information
  if ( mode == "pop")  {
    Undo('save');
    pos = ( (Undo.num+MAXSAVE-2) % MAXSAVE );
  	Undo.num = pos;
    // InfoWin(" --- Attempting to restore from slot " + pos + " ---\n");
  	if ( Undo.mol[pos][0] < 1 ) {
      alert("ERROR: No saved coordinates to restore.");
      return;
  	  }
  	}

  // Attempt to reverse last 'undo' (pop)
  if ( mode == "redo")  {
    pos = ( (Undo.num+1) % MAXSAVE );
  	Undo.num = pos;
    // InfoWin(" --- Attempting to go back to slot " + pos + " ---\n");
  	if ( Undo.mol[pos][0] < 1 ) {
      alert("ERROR: No saved coordinates to restore.");
      return;
  	  }
  	}

  if ( (mode == "redo") || (mode == "pop") )  {
    molecule[0].numatoms = Undo.mol[pos][0];
    for (i=1; i <= Undo.mol[pos][0]; i++) {
      molecule[i].atomicnumber = Undo.mol[pos][i].atomicnumber;
      molecule[i].x = Undo.mol[pos][i].x;
      molecule[i].y = Undo.mol[pos][i].y;
      molecule[i].z = Undo.mol[pos][i].z;
      molecule[i].charge = Undo.mol[pos][i].charge;
      molecule[i].highlite = Undo.mol[pos][i].highlite;
      }
    for (i=1; i <= molecule[0].numatoms; i++) {
      for (j=0; j <= molecule[0].numatoms; j++) {
        bonds[i][j] = Undo.bonds[pos][i][j];
        }
      }
    centerMolecule();
    drawMolecule();
    return;
    }

  // End of Undo routine
  }


//#   function addAtom(AtomicNum, x, y, z)
//#
//#   Routine to add atomic information to molecule array.
//#
//#   Parameters are the atomic # and (x,y,z) coordinates of the atom.
//#
function addAtom(AtomicNum, x, y, z, label) {

  // Declare local variables
  var i;
  var numatoms;
  var molecule = Mol();
  var bonds = BondMatrix();

  // Create/fill molecular array
  molecule[0].numatoms++;
  numatoms = molecule[0].numatoms;
  molecule[0].showcharges = 0;
  buttonColor("ChargeButton",0);
  molecule[numatoms] = new atomObject();
  molecule[numatoms].atomicnumber = AtomicNum;
  molecule[numatoms].x = x;
  molecule[numatoms].y = y;
  molecule[numatoms].z = z;
  molecule[numatoms].charge = 0.0;
  molecule[numatoms].label = label;
  molecule[numatoms].highlite = 0;

  // Initialize bond matrix
  if (typeof bonds[numatoms] === "undefined") {
    bonds[numatoms] = [];
    }
  bonds[numatoms][0] = 0;
  for (i=1; i <= numatoms; i++) {
    bonds[i][numatoms] = 0;
    bonds[numatoms][i] = 0;
    }

  // End of addAtom routine
  }


//#   function addBond(atom1, atom2)
//#
//#   Routine to add bonding information to bonds array
//#   (Note that atom numbers start at 1)
//#
function addBond(atom1, atom2) {

  // Define local variables
  var i, j;
  var newbond;
  var molecule = Mol();
  var numatoms = molecule[0].numatoms;
  var bonds = BondMatrix();

  // Add bonds to matrix
  bonds[atom1][0]++;
  bonds[atom1][atom2] = 1;
  bonds[atom2][0]++;
  bonds[atom2][atom1] = 1;

  // End of addBond routine
  }


//#   function delAtom(atomNum)
//#
//#   Routine to remove selected atom, directly-bonded Hydrogens, and
//#   cleanup molecule object (remove blank slots) and update bond arrays.
//#
//#   atomNum is the position of the atom to delete in the molecule array
//#
function delAtom(atomNum) {

  // Declare local variables
  var i, j, k, Hi=0;
  var bondedAtom, bi;
  var numatoms;
  var newNum, maxBonds, maxBondsB, maxBondsI, maxBondsJ;
  var HList = new Array();
  var molecule = Mol();
  var bonds = BondMatrix();

  // See if there are any attached hydrogen atoms
  molecule[0].showcharges = 0;
  buttonColor("ChargeButton",0);
  newNum = atomNum;
  for (i=1; i < atomNum; i++) {
    if ( (bonds[atomNum][i] > 0) && (molecule[i].atomicnumber == 1) ) {
      HList[Hi++] = i;
      newNum--;
      }
    }
  for (i=atomNum+1; i <= molecule[0].numatoms; i++) {
    if ( (bonds[atomNum][i] > 0) && (molecule[i].atomicnumber == 1) ) {
      HList[Hi++] = i;
      }
    }

  // Remove attached hydrogen atoms
  HList.sort(function(a,b){
    return(b-a);
    });
  for (i=0; i < Hi; i++) {
  	delAtom(HList[i]);
    }
  atomNum = newNum;

  // Remove atom and shift 'higher' atoms in molecule object to fill gaps
  for (i=atomNum; i < molecule[0].numatoms; i++) {
  	j=i+1;
    molecule[i].atomicnumber = molecule[j].atomicnumber;
    molecule[i].x = molecule[j].x;
    molecule[i].y = molecule[j].y;
    molecule[i].z = molecule[j].z;
    molecule[i].charge = molecule[j].charge;
    molecule[i].highlite = molecule[j].highlite;
    }
  molecule[0].numatoms--;

  // Remove bonds to atom being deleted
  numatoms = molecule[0].numatoms;
  for (i=1; i < atomNum; i++) {
    if ( bonds[i][atomNum] > 0 )
      bonds[i][0]--;
    for (j=atomNum; j <= numatoms; j++)
      bonds[i][j] = bonds[i][j+1];
    bonds[i][numatoms+1] = 0;
    }
  for (i=atomNum; i <= numatoms; i++) {
    if ( bonds[i+1][atomNum] > 0 )
      bonds[i+1][0]--;
    for (j=0; j < atomNum ; j++)
      bonds[i][j] = bonds[i+1][j];
    for (j=atomNum; j <= numatoms; j++)
      bonds[i][j] = bonds[i+1][j+1];
    bonds[i][numatoms+1] = 0;
    }
  for (i=0; i<=numatoms+1; i++)
    bonds[numatoms+1][i] = 0;

  // Finished with delAtom routine
  drawMolecule();
  }


//#   function delBond(atom1, atom2)
//#
//#   Routine to remove bond from bonds array.
//#
function delBond(atom1, atom2) {
  var i, maxBonds;
  var bonds = BondMatrix();

  // Remove bond on atom1
  if ( bonds[atom1][atom2] > 0 ) {
    bonds[atom1][atom2] = 0;
    bonds[atom1][0]--;
    }
  // Remove bond on atom2
  if ( bonds[atom2][atom1] > 0 ) {
    bonds[atom2][atom1] = 0;
    bonds[atom2][0]--;
    }

  // Finished with delBond routine
  }


//#   function hideH()
//#
//#   Do not display any hydrogen atoms in molecule
//#
function hideH() {
  var i;
  var molecule = Mol();

  // Loop over all atoms, setting hide flag to 0 for all atoms
  for (i=1; i <= molecule[0].numatoms; i++) {
    if ( molecule[i].atomicnumber == 1 ) {
      molecule[i].hide = 1;
      }
    }

  // Finished with hideH routine
  drawMolecule();
  }


//#   function showAll()
//#
//#   Show all atoms in molecule
//#
function showAll() {
  var i;
  var molecule = Mol();

  // Loop over all atoms, setting hide flag to 0 for all atoms
  for (i=1; i < molecule[0].numatoms; i++) {
    molecule[i].hide = 0;
    }


  // Finished with showAll routine
  }


//#   function centerMolecule()
//#
//#   Find center of molecule and move coordinates to center.
//#
function centerMolecule() {

  // Define local variables
  var i, A, numatoms;
  var molSize = 0.0;
  var xc, yc, zc;
  var xyz;
  var activeCanvas = activeWin("");
  var molecule = Mol();

  // Get height of Canvas
  var canvas = document.getElementById(activeCanvas);
  var height = canvas.height;

  // Find center of molecule
  xc = 0.0;
  yc = 0.0;
  zc = 0.0;
  numatoms = molecule[0].numatoms;
  for (i=1; i <= numatoms; i++) {
    xc += molecule[i].x;
    yc += molecule[i].y;
    zc += molecule[i].z;
    }
  xc /= numatoms;
  yc /= numatoms;
  zc /= numatoms;

  // Translate coordinates to center
  molSize = 0.0;
  for (i=1; i <= numatoms; i++) {
    A = molecule[i].atomicnumber;
    molecule[i].x -= xc;
    molecule[i].y -= yc;
    molecule[i].z -= zc;
    xyz = Math.abs(molecule[i].x);
    xyz = Math.max(xyz,Math.abs(molecule[i].y));
    xyz = Math.max(xyz,Math.abs(molecule[i].z));
    xyz += element(A,"radius");
    molSize = Math.max(molSize,xyz);
    }
  molecule[0].AtomScale = 0.5*height/molSize;

  // Finished with centerMolecule routine
  }


///
///   Display parameters (mainly for debugging)
///
function showGlobal() {

// Declare local variables
  var i;
  var molecule = Mol();

  InfoWin("numatoms = " + molecule[0].numatoms,1);
  InfoWin("\nAtomScale = " + molecule[0].AtomScale.toFixed(6));
  InfoWin("\n");

  for (i=1; i<=molecule[0].numatoms; i++) {
    A = molecule[i].atomicnumber;
    InfoWin(i + "  " + element(A,"symbol"));
    InfoWin(" (" + molecule[i].x.toFixed(4));
    InfoWin(", " + molecule[i].y.toFixed(4));
    InfoWin(", " + molecule[i].z.toFixed(4));
    InfoWin(")\n");
    }

}


//#   function showCoord(mode)
//#
//#   Display molecular coordinates and bonds in information window.
//#
//#   Parameter:
//#      mode=0:  Write .xyz formatted file
//#      mode>0:  Write coordinates and bond information
//#
function showCoord(mode) {

  // Declare local variables
  var i;
  var space;
  var molecule = Mol();
  var bonds = BondMatrix();

  // If no coordinates available, return
  if ( molecule[0].weight <= 0.0 )
    return;

  // Loop over all atoms and bonds
  if ( mode ) {
      InfoWin("Molecular Coordinates and Bond Information\n",1);
      InfoWin("   "+molecule[0].formula+"  ("+molecule[0].weight.toFixed(2)+" g/mol)");
      if ( (molecule[0].charge != 999) && (molecule[0].charge != 0) )
        InfoWin("   Charge = "+molecule[0].charge);
      InfoWin("\n");
    } else {
      InfoWin("Molecular Coordinates in .xyz format\n",1);
      InfoWin("--------------------\n");
      InfoWin(molecule[0].numatoms + "\n");
      InfoWin(molecule[0].formula+"  ("+molecule[0].weight.toFixed(2)+" g/mol) in xyz format: From CH5M3D\n");
    }
  for (i=1; i<=molecule[0].numatoms; i++) {
    space = "";
    if (i < 100)
      space = " ";
    if (i < 10)
      space = "  ";
    if ( mode ) {
      InfoWin(space+i+": ");
      }
    InfoWin(element(molecule[i].atomicnumber,"symbol") + " ");
    if ( element(molecule[i].atomicnumber,"symbol").length < 2 )
      InfoWin(" ");
    InfoWin(XYZpretty(molecule[i].x));
    InfoWin(XYZpretty(molecule[i].y));
    InfoWin(XYZpretty(molecule[i].z));
    if ( mode ) {
      InfoWin("  ");
      for (j=1; j <=molecule[0].numatoms; j++) {
        if ( bonds[i][j] > 0 )
          InfoWin("  "+j+",");
        }
      }
    InfoWin("\n");
    }

  // End of showCoord routine
  }


///
///   Helper routine to make coordinates line up in columns
///
function XYZpretty(coord) {
  // Declare local variables
  var space = "    ";
  var mystr = new Array();

  if ( coord >=  100.0) {
    mystr = space + " " + coord.toFixed(4);
    return mystr;
    }

  if ( coord >=   10.0) {
    mystr = space + "  " + coord.toFixed(4);
    return mystr;
    }

  if ( coord >=    0.0) {
    mystr = space + "   " + coord.toFixed(4);
    return mystr;
    }

  if ( coord >=  -10.0) {
    mystr = space + "  " + coord.toFixed(4);
    return mystr;
    }

  if ( coord >=  -100.0) {
    mystr = space + " " + coord.toFixed(4);
    return mystr;
    }

  mystr = space + coord.toFixed(4);
  return mystr;

  // Finished with XYZpretty
  }


//#   function formula()
//#
//#   Display molecular formula to division with an id = "formula".
//#   Note that the contents of this division will be overwritten.
//#
function formula() {
  var i, j, A;
  var found, num;
  var molweight;
  var molformula = new Array();
  var formulaStr="<p>Formula = ";
  var molecule = Mol();

  // If no molecule loaded, return
  if (molecule[0].numatoms < 1)
    return;

  // Look for carbon and place in first slot
  num = 0;
  for (i=1; i<=molecule[0].numatoms; i++)
    if ( molecule[i].atomicnumber == 6 ) {
      molformula[num] = [];
      molformula[num][0] = 6;
      molformula[num][1] = 0;
      num++;
      i = molecule[0].numatoms+1;
      }

  // Look for hydrogen in next slot
  for (i=1; i<=molecule[0].numatoms; i++)
    if ( molecule[i].atomicnumber == 1 ) {
      molformula[num] = [];
      molformula[num][0] = 1;
      molformula[num][1] = 0;
      num++;
      i = molecule[0].numatoms+1;
      }

  // Loop over all atoms in molecule
  for (i=1; i<=molecule[0].numatoms; i++) {
    A = molecule[i].atomicnumber;
    found = 0;
    for (j=0; j < num; j++) {
      if (molformula[j][0] == A) {
        molformula[j][1]++;
        found = 1;
        j = num;
        }
      }
    if (found == 0) {
      molformula[num] = new Array(2);
      molformula[num][0] = molecule[i].atomicnumber;
      molformula[num][1] = 1;
      num++;
      }
    }

  // Calculate molecular weight and output formula
  molweight = 0.0;
  molecule[0].formula = "";
  for (i=0; i<num; i++) {
    A = molformula[i][0];
    molweight += element(A,"mass") * molformula[i][1];
    formulaStr += element(A,"symbol");
    molecule[0].formula += element(A,"symbol");
    if (molformula[i][1] > 1) {
      formulaStr += "<sub>"+molformula[i][1]+"</sub>";
      molecule[0].formula += molformula[i][1] + " ";
      }
    }
  formulaStr += "</p>";
  molecule[0].weight = molweight;

  // Write formula to screen
  if ( document.getElementById("formula") )
    document.getElementById("formula").innerHTML = formulaStr;
  if ( molweight > 0.0 )
    InfoWin(molecule[0].formula+" has a molecular weight of "+molweight.toFixed(2)+"\n");

  // End formula routine
  }


//#   function RotateMolecule(axis)
//#
//#   Routine to start/stop rotation of molecule.
//#
//#   Parameter:
//#     axis = rotation axis.  Allowed values are "x", "y", or "z"
//#            ("s" can be used to stop all rotations)
//#
//#   Buttons must be created in html with:
//#     id="rotateX"  (or rotateY or rotateZ)
//#

  function RotateMolecule(axis) {
    // Declare local variables, auto rotate
    var delay = 20;  // Delay between redrawing screen, in ms

    // Parameter validation
    axis = axis[0].toLowerCase();
    if ( (axis != "x") &&  (axis != "y") && (axis != "z") && (axis != "s") ) {
      return;
      }

    // If first call, initialize "active" variable
    if(typeof RotateMolecule.RX === "undefined") {
      RotateMolecule.RX = 0;
      RotateMolecule.RY = 0;
      RotateMolecule.RZ = 0;
      }

    // Start/Stop rotation
    switch (axis) {
      case 'x':
                if ( RotateMolecule.RX == 0 ) {
                    // Start rotation
                    RotateMolecule.RX = 1;
                    RotateX_ID = setInterval( "rotateX()", delay );
                    buttonColor("rotateX",1);
                  } else {
                    // Stop rotation
                    RotateMolecule.RX = 0;
                    clearInterval( RotateX_ID );
                    buttonColor("rotateX",0);
                  }
                break;
      case 'y':
                if ( RotateMolecule.RY == 0 ) {
                    // Start rotation
                    RotateMolecule.RY = 1;
                    RotateY_ID = setInterval( "rotateY()", delay );
                    buttonColor("rotateY",1);
                  } else {
                    // Stop rotation
                    RotateMolecule.RY = 0;
                    clearInterval( RotateY_ID );
                    buttonColor("rotateY",0);
                  }
                break;
      case 'z':
                if ( RotateMolecule.RZ == 0 ) {
                    // Start rotation
                    RotateMolecule.RZ = 1;
                    RotateZ_ID = setInterval( "rotateZ()", delay );
                    buttonColor("rotateZ",1);
                  } else {
                    // Stop rotation
                    RotateMolecule.RZ = 0;
                    clearInterval( RotateZ_ID );
                    buttonColor("rotateZ",0);
                  }
                break;
      case 's':
                if ( RotateMolecule.RX != 0 ) {
                  RotateMolecule.RX = 0;
                  clearInterval( RotateX_ID);
                  }
                if ( RotateMolecule.RY != 0 ) {
                  RotateMolecule.RY = 0;
                  clearInterval( RotateY_ID);
                  }
                if ( RotateMolecule.RZ != 0 ) {
                  RotateMolecule.RZ = 0;
                  clearInterval( RotateZ_ID);
                  }
                buttonColor("rotateX",0);
                buttonColor("rotateY",0);
                buttonColor("rotateZ",0);
                break;
      }

    // End of RotateMolecule function
    }


//
//   Private function to perform rotation of molecule about x-axis
//
  function rotateX() {
    // Declare local variables
    var rot = 90;
    var i, y, z;
    var angle = 0.5;
    var cosA = Math.cos(-angle*Math.PI/rot);
    var sinA = Math.sin(-angle*Math.PI/rot);
    var molecule = Mol();

    // Draw molecule and display on canvas
    for (i=1; i <= molecule[0].numatoms; i++) {
      y = Math.round(molecule[i].y*10000)/10000;
      z = Math.round(molecule[i].z*10000)/10000;
      // console.log(z, y);
      molecule[i].y =  cosA*y - sinA*z;
      molecule[i].z = sinA*y + cosA*z;
      // console.log(molecule[i].y, molecule[i].z);
      }
    drawMolecule();

    // End of rotateX function
    }


//
//   Private function to perform rotation of molecule about y-axis
//
  function rotateY() {
    // Declare local variables
    var rot = 90;
    var i, x, y, z;
    var angle = 1;
    var cosA = Math.cos(-angle*Math.PI/rot);
    var sinA = Math.sin(-angle*Math.PI/rot);
    var molecule = Mol();

    // Draw molecule and display on canvas
    for (i=1; i <= molecule[0].numatoms; i++) {
      x = Math.round(molecule[i].x*10000)/10000;
      z = Math.round(molecule[i].z*10000)/10000;
      molecule[i].x =  sinA*z + cosA*x;
      molecule[i].z = cosA*z - sinA*x ;
      }
    drawMolecule();

    // End of rotateY function
    }


//
//   Private function to perform rotation of molecule about z-axis
//
  function rotateZ() {
    // Declare local variables
    var rot = 90;
    var i, x, y, z;
    var angle = 1;
    var cosA = Math.cos(-angle*Math.PI/rot);
    var sinA = Math.sin(-angle*Math.PI/rot);
    var molecule = Mol();

    // Draw molecule and display on canvas
    for (i=1; i <= molecule[0].numatoms; i++) {
      x = Math.round(molecule[i].x*10000)/10000;
      y = Math.round(molecule[i].y*10000)/10000;
      molecule[i].x =  cosA*x - sinA*y;
      molecule[i].y = sinA*x + cosA*y;
      }
    drawMolecule();

    // End of rotateZ function
    }
//
// -------------------- drawmolecule.js --------------------
//

//#   function drawMolecule()
//#
//#   Draw atoms and bonds.
//#
function drawMolecule() {

  // Define local variables
  var i, j, k;
  var x, y, r;
  var bonds = BondMatrix();
  var molecule = Mol();
  var A, numatoms=molecule[0].numatoms;
  var bondto, maxBonds;
  var x1, y1, x2, y2;
  var AtomSize = 0.30; // set size in atomdraw   the same
  var SimpleSwitch = 250;

  // Create connection to active Canvas
  var mycanvas = activeWin("");
  var canvas = document.getElementById(mycanvas);
  if ( ! canvas )
    return;
  var ctx = canvas.getContext('2d');
  var width = canvas.width;
  var height = canvas.height;
  var centerx = canvas.width/2;
  var centery = canvas.height/2;

  // Clear screen before drawing molecule
  clear(ctx, width, height);

  // Define properties of lines
  ctx.strokeStyle = "rgb(0, 0, 255)";
  ctx.lineWidth = 3;
  ctx.lineCap = 'round'; // line Cap for bonds
  //ctx.lineJoin = 'bevel';
  // Depth sort: Draw from back to front
  if ( typeof drawMolecule.deep == 'undefined' ) {
    drawMolecule.deep = [];
    }
  if ( drawMolecule.deep.length != numatoms ) {
    j=0;
    drawMolecule.deep = [];
    for (i=drawMolecule.deep.length; i<numatoms; i++) {
      j++;
      drawMolecule.deep[i] = [];
      drawMolecule.deep[i]["id"] = j;
      drawMolecule.deep[i]["sz"] = molecule[j].z;
      }
    }
  for (i=0; i<numatoms; i++) {
    j = drawMolecule.deep[i].id;
    drawMolecule.deep[i].z = molecule[j].z;
    }
  drawMolecule.deep.sort(function(a,b){
    return(b.z - a.z);
    });

  // If too many atoms, do not use gradients
  if ( numatoms > SimpleSwitch )
    molecule[0].gradients = 0;

  // Loop over all atoms in molecule
  for (i = 0; i < numatoms; i++) {
    atom = drawMolecule.deep[i].id;
    if ( ! molecule[atom].hide ) {
      if ( molecule[0].gradients ) {
          drawAtom(ctx, atom, AtomSize, centerx, centery);
        } else {
          drawAtomPlain(ctx, atom, AtomSize, centerx, centery);
        }
      if ( molecule[0].showcharges != 0 )
        DrawChargeCloud(ctx, atom, AtomSize*1.5, centerx, centery);
      if ( molecule[atom].highlite != 0 )
        DrawAtomHilite(ctx, atom, AtomSize*1.5, centerx, centery);
      // Loop over all bonds on current atom
      for (j = 1; j <= numatoms; j++) {
        if ( (bonds[atom][j] > 0) && (j != atom) && !molecule[j].hide ) {
          for (k=i+1; k < numatoms; k++) {
            if (drawMolecule.deep[k].id == j) {
              //console.log(molecule[0].gradients)
              drawBond(ctx, atom, j, AtomSize, centerx, centery, molecule[0].gradients);
              }
            }
          }
        }
      }
    }

  // Finished with drawMolecule routine
  }


//#   function showLabels()
//#
//#   Routine to toggle display of atomic labels.
//#
function showLabels() {

  // Local variables
  var molecule = Mol();

  if ( molecule[0].showlabels == 0 ) {
    buttonColor("LabelButton",1);
    molecule[0].showlabels = 1;
    drawMolecule();
    return;
    }
  buttonColor("LabelButton",0);
  molecule[0].showlabels = 0;
  drawMolecule();
  return;
  }



///
///   Routine to draw a single atom
///
function drawAtom(ctx, atomNum, AtomSize, centerx, centery) {
  // Define local variables
  var A;
  var x, y, r;
  var label;
  var xoff, yoff, roff;
  var molecule = Mol();
  var activeCanvas = activeWin("");

  // Get parameters for atom
  A = molecule[atomNum].atomicnumber;
//  console.log(molecule[0]);
  x = molecule[0].AtomScale*molecule[atomNum].x + centerx;
  y = molecule[0].AtomScale*molecule[atomNum].y + centery;
  r = molecule[0].AtomScale*AtomSize*element(A,"radius");
  label = molecule[0].AtomScale*molecule[atomNum].label;
  xoff = x-(0.20*r);
  yoff = y-(0.20*r);
  roff = 0.3*r;
  x = Math.floor(x+0.5);
  y = Math.floor(y+0.5);
  r = Math.floor(r+0.5);
  xoff = Math.floor(xoff+0.5);
  yoff = Math.floor(yoff+0.5);
//  console.log(x, y, r)
  AtomColor = ctx.createRadialGradient(xoff, yoff, roff, x, y, r);
  AtomColor.addColorStop(0, element(A,"color"));
  AtomColor.addColorStop(1, element(A,"gradient"));

  // Plot atom as a gradient shaded circle
  ctx.beginPath();
  ctx.arc(x, y, r, 0, 2*Math.PI, false);
  ctx.fillStyle = AtomColor;
  ctx.fill();
  ctx.lineWidth = 1;
  ctx.strokeStyle = "black";
  ctx.stroke();
  ctx.closePath();
  // Draw label for atom
  if ( molecule[0].showlabels != 0 )
    //console.log(A,atomNum,x,y);
    atomLabel(ctx,A,atomNum,x,y, label);

  // End of drawAtom routine
  }


///
///   Routine to draw a single atom without gradient
///
function drawAtomPlain(ctx, atomNum, AtomSize, centerx, centery) {
  // Define local variables
  var A;
  var x, y, r;
  var xoff, yoff, roff;
  var molecule = Mol();
  var activeCanvas = activeWin("");

  // Get parameters for atom
  A = molecule[atomNum].atomicnumber;
  x = molecule[0].AtomScale*molecule[atomNum].x + centerx;
  y = molecule[0].AtomScale*molecule[atomNum].y + centery;
  r = molecule[0].AtomScale*AtomSize*element(A,"radius");
  xoff = x-(0.10*r);
  yoff = y-(0.10*r);
  roff = 0.30*r;
  x = Math.floor(x+0.5);
  y = Math.floor(y+0.5);
  r = Math.floor(r+0.5);
  xoff = Math.floor(xoff+0.5);
  yoff = Math.floor(yoff+0.5);

  // Plot atom as a solid shaded circle
  ctx.beginPath();
  ctx.arc(x, y, r, 0, 2*Math.PI, false);
  ctx.fillStyle = element(A,"color");
  ctx.fill();
  ctx.lineWidth = 1;
  ctx.strokeStyle = "black";
  ctx.stroke();
  ctx.closePath();

  // Draw label for atom
  if ( molecule[0].showlabels != 0 )
    atomLabel(ctx,A,atomNum,x,y);

  // End of drawAtomPlain routine
  }


///
///   Routine to draw charge cloud around a single atom
///
function DrawChargeCloud(ctx, atomNum, AtomSize, centerx, centery) {
  // Define local variables
  var A;
  var x, y, r;
  var colR, colB, colG, deltaRGB;
  var molecule = Mol();
  var activeCanvas = activeWin("");

  // Get parameters for atom
  A = molecule[atomNum].atomicnumber;
  x = molecule[0].AtomScale*molecule[atomNum].x + centerx;
  y = molecule[0].AtomScale*molecule[atomNum].y + centery;
  r = molecule[0].AtomScale*AtomSize*element(A,"radius");

  // Set colors based on charge
  var q = molecule[atomNum].charge;
  // Positive charges shown in blue
  if (q >= 0) {
    (q > 1.0) ? deltaRGB = 1.0 : deltaRGB = q;
    colR =   0;
    colG =   0;
    colB = 255;
    }
  // Positive charges shown in red
  if (q < 0) {
    (q < -1.0) ? deltaRGB = 1.0 : deltaRGB = -q;
    colR = 255;
    colG =   0;
    colB =   0;
    }
  AtomColor = "rgba("+colR+","+colG+","+colB+","+deltaRGB+")";
//    AtomColor = "rgba("+colR+","+colG+","+colB+",0.75)";

  // Plot charge cloud as a semi-transparent circle
  ctx.beginPath();
  ctx.arc(x, y, r, 0, 2*Math.PI, false);
  ctx.fillStyle = AtomColor;
  ctx.fill();
  ctx.lineWidth = 0.01;
  ctx.strokeStyle = "black";
  ctx.stroke();
  ctx.closePath();

  // End DrawChargeCloud routine
  }


///
///   Routine to draw a single atom with a highlight
///
function DrawAtomHilite(ctx, atomNum, AtomSize, centerx, centery) {

  // Define local variables
  var A;
  var x, y, r;
  var colR, colB, colG, deltaRGB;
  var molecule = Mol();
  var activeCanvas = activeWin("");

  // Get parameters for atom
  A = molecule[atomNum].atomicnumber;
  x = molecule[0].AtomScale*molecule[atomNum].x + centerx;
  y = molecule[0].AtomScale*molecule[atomNum].y + centery;
  r = molecule[0].AtomScale*AtomSize*element(A,"radius");

  // Set highlight color to yellow
  AtomColor = "rgba(255,255,0,0.5)";

  // Plot charge cloud as a semi-transparent circle
  ctx.beginPath();
  ctx.arc(x, y, r, 0, 2*Math.PI, false);
  ctx.fillStyle = AtomColor;
  ctx.fill();
  ctx.lineWidth = 0.01;
  ctx.strokeStyle = "black";
  ctx.stroke();
  ctx.closePath();

  // End DrawAtomHilite routine
  }


///
///   Helper routine to draw label for atom
///   Parameters:
///     Atomic number, atom #, (x,y) coordinates
///
function atomLabel(ctx,A,i,ax,ay, label) {
  var label = element(A,"symbol");
  var fontsize = 14;
  var x = parseFloat(ax);
  var y = parseFloat(ay) + fontsize/2;
  var molecule = Mol();

  ctx.lineWidth = 1.0;
  ctx.textAlign = "center";
  ctx.font = "normal " + fontsize + "px sans-serif";
  ctx.fillStyle = element(A,"label");
  ctx.beginPath();
  ctx.fillText(label,x,y);
  var w = 10.0 / molecule[0].AtomScale;
  ctx.fillRect(x,y,w*1.5,w);
  ctx.closePath();
  }


///
///   Routine to draw a single bond
///
function drawBond(ctx, atom1, atom2, AtomSize, centerx, centery, smallMolecule) {

  // Define local variables
  var i, j, k;
  var x1, y1, z1, x2, y2, z2;
  var dx, dy, dz;
  var xoff, yoff;
  var dist, r;
  var molecule = Mol();
  var activeCanvas = activeWin("");
  var AtomScale = molecule[0].AtomScale;
  var BondWidth = Math.floor(0.1*AtomScale + 0.2); // bond thickness
  var BondColor = "rgb(60,60,60)";

  // Get parameters for atoms
  r =  AtomScale * AtomSize * element(molecule[atom1].atomicnumber,"radius") -2;
  x1 = AtomScale*molecule[atom1].x + centerx;
  y1 = AtomScale*molecule[atom1].y + centery;
  z1 = AtomScale*molecule[atom1].z;
  x2 = AtomScale*molecule[atom2].x + centerx;
  y2 = AtomScale*molecule[atom2].y + centery;
  z2 = AtomScale*molecule[atom2].z;

  // For large molecules, use simpler plot
  if ( ! smallMolecule ) {
    ctx.beginPath();
    ctx.moveTo(xoff, yoff);
    ctx.lineTo(x2, y2);
    ctx.lineWidth = BondWidth;
    ctx.strokeStyle = BondColor;
    ctx.stroke();
    ctx.closePath();
    }


  // Calculate intersection of bond with sphere
  dx = x2 - x1;
  dy = y2 - y1;
  dz = z2 - z1;
  dist = Math.sqrt(dx*dx + dy*dy + dz*dz);
  xoff = x1 + r*dx/dist;
  yoff = y1 + r*dy/dist;

  // Draw bond
  ctx.beginPath();
  ctx.moveTo(xoff, yoff);
  ctx.lineTo(x2, y2);
  ctx.lineWidth = BondWidth;
  ctx.strokeStyle =  BondColor;
  ctx.stroke();
  ctx.closePath();
  }


///
///   Clear drawing window (canvas)
///
function clear(ctx, width, height) {
  // Clear plot area
  ctx.fillStyle = "rgb(255,255,255)";
  ctx.fillRect(0, 0, width, height);
  // ctx.clearRect(0, 0, width, height);

  // Show border around plot area
  ctx.beginPath();
  ctx.rect(1,1,width-1,height-1);
  ctx.lineWidth = 2;
  ctx.strokeStyle = "rgb(240,240,240)";
  ctx.stroke();
  ctx.closePath();
  }


///
///   Draw atoms and bonds with highlighting
///
function drawHighlight(mycanvas, sequence, AtomSize, centerx, centery) {

  // Define local variables
  var i, j, k;
  var x, y, r;
  var A;
  var maxBonds, bondto;
  var x1, y1, x2, y2;
  var molecule = Mol();
  var bonds = BondMatrix();

  // Create connection to Canvas
  var canvas = document.getElementById(mycanvas);
  var ctx = canvas.getContext('2d');
  var width = canvas.width;
  var height = canvas.height;

  // Clear screen before drawing molecule
  clear(ctx, width, height);

  // Define properties of lines
  ctx.strokeStyle = "rgb(0, 0, 255)";
  ctx.lineWidth = 2.0;

  // Depth sort: Draw from back to front
  if ( typeof drawHighlight.deep == 'undefined' ) {
    drawHighlight.deep = [];
    }
  if ( drawHighlight.deep.length != molecule[0].numatoms ) {
    j=0;
    drawHighlight.deep = [];
    for (i=drawHighlight.deep.length; i<molecule[0].numatoms; i++) {
      j++;
      drawHighlight.deep[i] = [];
      drawHighlight.deep[i]["id"] = j;
      drawHighlight.deep[i]["sz"] = molecule[j].z;
      }
    }
  for (i=0; i<molecule[0].numatoms; i++) {
    j = drawHighlight.deep[i].id;
    drawHighlight.deep[i].z = molecule[j].z;
    }
  drawHighlight.deep.sort(function(a,b){
    return(b.z - a.z);
    });

  // Loop over all atoms in molecule
  for (i = 0; i < molecule[0].numatoms; i++) {
    atom = drawHighlight.deep[i].id;
    hilite = 0;
    for (ih=1; ih <= sequence[0]*3; ih++) {
      if (atom == sequence[ih])
        hilite = 1;
      }
    HighlightAtom(ctx, atom, hilite, AtomSize, centerx, centery);
    // Loop over all bonds on current atom
    for (bondto = 1; bondto <= molecule[0].numatoms; bondto++) {
      if ( bonds[atom][bondto] > 0) {
        highbond = 0;
        if (hilite > 0) {
          for (ih=1; ih < sequence[0]*3; ih++) {
            if (bondto == sequence[ih])
              highbond = 1;
            }
          }
        for (k=i+1; k < molecule[0].numatoms; k++) {
          if (drawHighlight.deep[k].id == bondto) {
            HighlightBond(ctx,atom,bondto,highbond, AtomSize, centerx, centery);
            }
          }
        }
      }
    }

  // Finished with drawHighlight routine
  }


///
///   Routine to draw a single highlighted atom
///
function HighlightAtom(ctx, atomNum, hilite, AtomSize, centerx, centery) {
  // Define local variables
  var A;
  var x, y, r;
  var xoff, yoff, roff;
  var istart, ilength, colorstr;
  var myrgb = new Array();
  var bcolor = "rgb(191,191,191)";
  var hcolor = "rgb(255,  0,  0)";
  var gcolor = "rgb(127,  0,  0)";
  var molecule = Mol();
  var activeCanvas = activeWin("");

  // Get parameters for atom
  A = molecule[atomNum].atomicnumber;
  x = molecule[0].AtomScale*molecule[atomNum].x + centerx;
  y = molecule[0].AtomScale*molecule[atomNum].y + centery;
  r = molecule[0].AtomScale*AtomSize*element(A,"radius");
  xoff = x-(0.20*r);
  yoff = y-(0.20*r);
  roff = 0.30*r;
  x = Math.floor(x+0.5);
  y = Math.floor(y+0.5);
  r = Math.floor(r+0.5);
  xoff = Math.floor(xoff+0.5);
  yoff = Math.floor(yoff+0.5);
  AtomColor = ctx.createRadialGradient(xoff, yoff, roff, x, y, r);

  alpha = 0.33;
  if (hilite > 0)
    alpha = 1.0;
  istart  = element(A,"color").indexOf("(") + 1;
  ilength = element(A,"color").indexOf(")") - istart;
  colorstr = element(A,"color").substr(istart,ilength);
  myrgb = colorstr.replace(/,/g," ").split(' ');
  hcolor = "rgba("+myrgb[0]+","+myrgb[1]+","+myrgb[2]+","+alpha+")";
  istart  = element(A,"gradient").indexOf("(") + 1;
  ilength = element(A,"gradient").indexOf(")") - istart;
  colorstr = element(A,"gradient").substr(istart,ilength);
  myrgb = colorstr.replace(/,/g," ").split(' ');
  gcolor = "rgba("+myrgb[0]+","+myrgb[1]+","+myrgb[2]+","+alpha+")";
  AtomColor.addColorStop(0, hcolor);
  AtomColor.addColorStop(1, gcolor);

  // Plot atom as a gradient shaded circle
  ctx.beginPath();
  ctx.arc(x, y, r, 0, 2*Math.PI, false);
  ctx.fillStyle = AtomColor;
  ctx.fill();
  ctx.lineWidth = 0.01;
  ctx.strokeStyle = "black";
  ctx.stroke();
  ctx.closePath();

  // Draw label if highlighted atom
  if (hilite > 0)
    atomLabel(ctx,A,atomNum,x,y);
  }


///
///   Routine to draw a single highlighted bond
///
function HighlightBond(ctx, atom1, atom2, highlite, AtomSize, centerx, centery) {
  // Define local variables
  var i, j, k;
  var x1, y1, z1, x2, y2, z2;
  var dx, dy, dz;
  var xoff, yoff;
  var dist, r;
  var AtomScale = molecule[0].AtomScale;
  var BondWidth = Math.floor(0.10*AtomScale + 0.5);
  var BondColor = "rgba(200,128,51,1.0)";
  var bcolor = "rgba(191,191,191,0.33)";
  var molecule = Mol();
  var activeCanvas = activeWin("");

  // Get parameters for atoms
  r = AtomScale * AtomSize * element(molecule[atom1].atomicnumber,"radius");
  x1 = AtomScale*molecule[atom1].x + centerx;
  y1 = AtomScale*molecule[atom1].y + centery;
  z1 = AtomScale*molecule[atom1].z;
  x2 = AtomScale*molecule[atom2].x + centerx;
  y2 = AtomScale*molecule[atom2].y + centery;
  z2 = AtomScale*molecule[atom2].z;

  // Calculate intersection of bond with sphere
  dx = x2 - x1;
  dy = y2 - y1;
  dz = z2 - z1;
  dist = Math.sqrt(dx*dx + dy*dy + dz*dz);
  xoff = x1 + r*dx/dist;
  yoff = y1 + r*dy/dist;

  // Draw bond
  ctx.beginPath();
  ctx.moveTo(xoff, yoff);
  ctx.lineTo(x2, y2);
  ctx.lineWidth = BondWidth + 2;
  ctx.strokeStyle = "rgba(0,0,0,0.33)";
  if ( highlite > 0 )
    ctx.strokeStyle = "rgba(0,0,0,1.0)";
  ctx.stroke();
  ctx.moveTo(xoff, yoff);
  ctx.lineTo(x2, y2);
  ctx.lineWidth = BondWidth;
  if ( highlite > 0 ) {
      ctx.strokeStyle = BondColor;
    } else {
      ctx.strokeStyle = bcolor;
    }
  ctx.stroke();
  ctx.closePath();
  }
// -------------------- mouse.js file --------------------

///
///   Routine to save number of atom selected with mouseDown event
///   option = "Set" or "Show"
///   value  = Number of selected atom
///        0 = MouseDown, but not on atom
///       -1 = Mouse not down
///
function mouseState(option, value) {
  // Initialize parameters as necessary
  if ( typeof mouseState.DownAtom == 'undefined' )
    mouseState.DownAtom = -1;

  // Show number of atom selected by mouseDown
  if ( option == "Show" )
    return mouseState.DownAtom;

  if ( option == "Set" )
    mouseState.DownAtom = value;

  // End of mouseState routine
  }


//#   function parameters()
//#
//#   Define constants used to control drawing.
//#   Get/set values using:
//#      var param = parameters();
//#
//#    param.mode   = Interface mode.  Set to "Draw" or "View"
//#    param.element   = Type of element to add next.  Default = "C"
//#    param.clouds = # of hybrid orbitals.  Default = 4
//#    param.bondmode   = Bond mode.  Set to "Add", "Delete", or "Rotate"
//#    param.atommode    = Add atom mode.  Set to "Add" or "Delete"
//#
function parameters() {

  // Initialize parameter array if necessary
  if ( typeof parameters.values === "undefined" )
    parameters.values = new paramObject();

  // Define default values for parameters
  if ( typeof parameters.values.mode == 'undefined' )
    parameters.values.mode = "View";
  if ( typeof parameters.values.elem == 'undefined' )
    parameters.values.elem = "C";
  if ( typeof parameters.values.clouds == 'undefined' )
    parameters.values.clouds = 4;
  if ( typeof parameters.values.add == 'undefined' )
    parameters.values.add = "Add";
  if ( typeof parameters.values.bond == 'undefined' )
    parameters.values.bond = "Add";

  // End of parameters routine
  return parameters.values;
  }


///
///   Define structure for drawing parameters
///
function paramObject() {
  this.mode = "View";
  this.element = "C";
  this.clouds = 4;
  this.bondmode = "Add";
  this.atommode = "Add";
  }


///
///   Routine to handle mouse press
///
function MouseDown(evt) {
  // Declare local variables
  var cx, cy;
  var windowName = evt.target.id;
  var activecanvas = activeWin(windowName);
  var canvas = document.getElementById(activecanvas);
  var width = canvas.width;
  var height = canvas.height;

  // Map touch screen and mouse buttons
  cx = evt.pageX;
  cy = evt.pageY;
  // If touch screen
  if (evt.targetTouches) {
    if (evt.targetTouches.length == 1) {
      cx = evt.targetTouches[0].pageX;
      cy = evt.targetTouches[0].pageY;
      }
    }

  // Save selected atom
  mouseState( "Set", onAtom(cx, cy, canvas, width, height) );
  }


///
///   Routine to handle mouse up
///
function MouseUp(evt) {
  // Declare local variables
  var cx, cy;
  var mouseOnAtom, UpAtom;
  var activecanvas = activeWin("");
  var molecule = Mol();
  var canvas = document.getElementById(activecanvas);
  var width = canvas.width;
  var height = canvas.height;
  var param = parameters();

  // Map touch screen and mouse buttons
  cx = evt.pageX;
  cy = evt.pageY;
  // If touch screen
  if (evt.targetTouches) {
    cx = evt.targetTouches[0].pageX;
    cy = evt.targetTouches[0].pageY;
    }

  // See which atom (if any) mouse is currently on
  mouseOnAtom = mouseState("Show");
  mouseState("Set", -1);
  Upatom = onAtom(cx, cy, canvas, width, height);

  // If 'click' moves to blank space, exit
  if ( Upatom == 0 ) {
    viewGeom(0);
    return;
    }

  // If 'click' stays on a same atom, proceed
  if ( Upatom == mouseOnAtom ) {
    // Show geometry information
    if (param.mode == "View") {
      if ( evt.shiftKey > 0) {
          molecule[Upatom].highlite = ( (molecule[Upatom].highlite+1) % 2);
          drawMolecule();

        } else {
          viewGeom(mouseOnAtom);
          }
      }
    // Add or Remove atom(s)
    if (param.mode == "Draw") {
      // Save Molecular information
      Undo("save");
      molecule[0].charge = 999;
      if (param.atommode == "Delete") {
          delAtom(Upatom);
        } else {
          newAtom(Upatom);
        }
      }
    }

  // If 'click' moves to a different atom, draw or remove bond
  if ( (Upatom != mouseOnAtom) && (param.mode == "Draw") ) {
    // Save Molecular information
    Undo("save");
    if (param.bondmode == "Add") {
      molecule[0].charge = 999;
      addBond(mouseOnAtom,Upatom);
      }
    if (param.bondmode == "Delete") {
      molecule[0].charge = 999;
      delBond(mouseOnAtom,Upatom);
      }
    if (param.bondmode == "Rotate") {
      BondRotation("Set",mouseOnAtom,Upatom);
      }
    drawMolecule();
    }

  // Finished with MouseUp routine
  }


///
///   Is mouse within radius of atom?
///   Parameters - mouse coordinates
///   Return - number of atom or zero if none
///
function onAtom(mx, my, canvas, width, height) {
  // Declare local variables
  var i, A, dx, dy;
  var radius, delta;
  var AtomSize = 0.30;
  var molecule = Mol();

  // Convert mouse position to atomic coordinate system
  mx = (mx - canvas.offsetLeft - width/2);
  my = (my - canvas.offsetTop - height/2);

  // Loop over all atoms, looking for first match
  for (i=1; i <= molecule[0].numatoms; i++) {
    A = molecule[i].atomicnumber;
    radius = molecule[0].AtomScale*AtomSize*element(A,"radius");
    radius = radius*radius;
    dx = molecule[0].AtomScale*molecule[i].x - mx;
    dy = molecule[0].AtomScale*molecule[i].y - my;
    delta = dx*dx + dy*dy;
    if (delta <= radius) {
      return i;
      }
    }
  return 0;
  }


///
///   Routine to deal with scroll wheel
///
function MouseWheel(evt) {

  // Local variable
  var molecule = Mol();

  // Stop window scrolling
  if (evt.preventDefault)
    evt.preventDefault();

  //  Firefox and Opera use detail, Chrome uses wheelDelta(?)
  var delta = evt.detail ? evt.detail*(-1) : evt.wheelDelta;
  var newScale = (delta > 0) ? 1.1 : 0.9;
  molecule[0].AtomScale = molecule[0].AtomScale*newScale;
  drawMolecule();
  return false;
  }


///
///   Alter molecule IFF mouse is pressed
///
function MouseMove(evt) {
  var newx, newy;
  var dx, dy, tx, ty, da;
  var x, y, z;
  var xc, yc;
  var cosx, cosy, cosz, sinx, siny, sinz;
  var cosA, sinA;
  var step=4;  // Smaller values make less sensitive
  var molecule = Mol();
  var param = parameters();

  // Save old (x,y) coordinates
  if ( typeof MouseMove.cx == 'undefined' )
    MouseMove.cx = 100;
  if ( typeof MouseMove.cy == 'undefined' )
    MouseMove.cy = 100;

  // Only rotate if mouse pressed, but not on an atom
  if ( mouseState("Show") == 0 ) {
    
    // Map touch screen and mouse buttons
    newx = evt.pageX;
    newy = evt.pageY;
    // If touch screen
    if (evt.targetTouches) {
      if (evt.targetTouches.length == 1) { // -1/50 smoothing
        newx = evt.targetTouches[0].pageX* -1 / 60;
        newy = evt.targetTouches[0].pageY* -1 / 60;
        }
      }

    // Record movement
    dx = (MouseMove.cx - newx);
    dy = (MouseMove.cy - newy);
    MouseMove.cx = newx;
    MouseMove.cy = newy;
    if ( Math.abs(dx)+Math.abs(dy) > 10)
      return;

    // Handle special case of rotation about a bond
    if ( param.bondmode == "Rotate" ) {
      da = dx + dy;
      BondRotation("Rotate",da);
      drawMolecule();
      return;
      }

    // If <Shift> key pressed, rotate around z-axis
    if ( evt.shiftKey > 0) {
      cosz = Math.cos(dx*step*Math.PI/180);
      sinz = Math.sin(dx*step*Math.PI/180);
      for (i=1; i <= molecule[0].numatoms; i++) {
        x = molecule[i].x;
        y = molecule[i].y;
        molecule[i].x =  cosz*x + sinz*y;
        molecule[i].y = -sinz*x + cosz*y;
        }
      drawMolecule();
      return;
      }

    // If <Ctrl> key pressed, translate along x- or y-axis
    if ( evt.ctrlKey > 0) {
      tx = dx*0.001;
      ty = dy*0.001;
      for (i=1; i <= molecule[0].numatoms; i++) {
        x = molecule[i].x;
        y = molecule[i].y;
        molecule[i].x = x - tx;
        molecule[i].y = y - ty;
        }
      drawMolecule();
      return;
      }

    // Rotate entire molecule
    cosx = Math.cos(dy*step*Math.PI/180);
    sinx = Math.sin(dy*step*Math.PI/180);
    cosy = Math.cos(dx*step*Math.PI/180);
    siny = Math.sin(dx*step*Math.PI/180);
    for (i=1; i <= molecule[0].numatoms; i++) {
      x = molecule[i].x;
      y = molecule[i].y;
      z = molecule[i].z;
      molecule[i].x =  cosy*x + siny*z;
      molecule[i].y = -sinx*siny*x + cosx*y + sinx*cosy*z;
      molecule[i].z = -cosx*siny*x - sinx*y + cosx*cosy*z;
      }
    drawMolecule();
    }
  }


///
///   VIEW MODE: Routine to display geometry information to user
///
function viewGeom(OnAtom) {
  // Declare local variables
  var i, A1, A2, A3, A4;
  var dx, dy, dz, d;
  var dux, duy, duz, dvx, dvy, dvz, du, dv;
  var label;
  var activecanvas = activeWin("");
  var canvas = document.getElementById(activecanvas);
  var ctx = canvas.getContext('2d');
  var width = canvas.width;
  var height = canvas.height;
  var molecule = Mol();

  // Initialize geom array if necessary
  if ( typeof viewGeom.geom == 'undefined' ) {
    viewGeom.geom = [0,0,0,0,0];
    }

  // If valid atom not sent, zero array
  if (OnAtom == 0) {
    for (i=0; i < 5; i++)
      viewGeom.geom[i] = 0;
    drawMolecule();
    return;
    }

  // If duplicate atom sent, zero array and return
  if (OnAtom) {
    for (i=1; i < 5; i++) {
      if (viewGeom.geom[i] == OnAtom)
        viewGeom(0);
      }
    }

  // Display appropriate information to user
  viewGeom.geom[0] = viewGeom.geom[0] + 1;
  sw = viewGeom.geom[0];
  viewGeom.geom[sw] = OnAtom;
//InfoWin("\nMouse on atom #"+OnAtom+"   Switch = "+sw);
  switch (sw) {
    case 1:
        A1 = molecule[viewGeom.geom[1]].atomicnumber;
        label = element(A1,"symbol") + viewGeom.geom[1].toString();
        if ( molecule[0].showcharges != 0 ) {
          label += ": Charge = ";
          if ( molecule[viewGeom.geom[1]].charge > 0 )
            label += "+";
          label += molecule[viewGeom.geom[1]].charge.toFixed(2);
          }
        drawMolecule();
        geomLabel(ctx,label,width);
        break;
    case 2:
        // Bond distance
        dx = molecule[viewGeom.geom[1]].x - molecule[viewGeom.geom[2]].x;
        dy = molecule[viewGeom.geom[1]].y - molecule[viewGeom.geom[2]].y;
        dz = molecule[viewGeom.geom[1]].z - molecule[viewGeom.geom[2]].z;
        d = Math.sqrt(dx*dx+dy*dy+dz*dz);
        d = d.toFixed(3);
        d = d.toString();
        A1 = molecule[viewGeom.geom[1]].atomicnumber;
        A2 = molecule[viewGeom.geom[2]].atomicnumber;
        label  = element(A1,"symbol") + viewGeom.geom[1].toString() + "--";
        label += element(A2,"symbol") + viewGeom.geom[2].toString();
        label += " = " + d;
        drawMolecule();
        geomLabel(ctx,label,width);
        break;
    case 3:
        // Bond angle
        A1 = molecule[viewGeom.geom[1]].atomicnumber;
        A2 = molecule[viewGeom.geom[2]].atomicnumber;
        A3 = molecule[viewGeom.geom[3]].atomicnumber;
        label  = element(A1,"symbol") + viewGeom.geom[1].toString() + "--";
        label += element(A2,"symbol") + viewGeom.geom[2].toString() + "--";
        label += element(A3,"symbol") + viewGeom.geom[3].toString();
        ang = angle(molecule,viewGeom.geom[1],viewGeom.geom[2],viewGeom.geom[3]);
        ang = ang.toFixed(1);
        ang = ang.toString();
        label += " = " + ang + "ᵒ";
        drawMolecule();
        geomLabel(ctx,label,width);
        break;
    case 4:
        // Dihedral angle
        A1 = molecule[viewGeom.geom[1]].atomicnumber;
        A2 = molecule[viewGeom.geom[2]].atomicnumber;
        A3 = molecule[viewGeom.geom[3]].atomicnumber;
        A4 = molecule[viewGeom.geom[4]].atomicnumber;
        label  = element(A1,"symbol") + viewGeom.geom[1].toString() + "--";
        label += element(A2,"symbol") + viewGeom.geom[2].toString() + "--";
        label += element(A3,"symbol") + viewGeom.geom[3].toString() + "--";
        label += element(A4,"symbol") + viewGeom.geom[4].toString();
        ang = dihedral(molecule,viewGeom.geom[1],viewGeom.geom[2],viewGeom.geom[3],viewGeom.geom[4]);
        ang = ang.toFixed(1);
        ang = ang.toString();
        label += " = " + ang;
        drawMolecule();
        geomLabel(ctx,label,width);
        for (i=0; i < 5; i++)
          viewGeom.geom[i] = 0;
        break;
      }
  }


///
///   VIEW MODE:
///   Helper routine to show geometry information
///   Parameters - mouse coordinates
///
function geomLabel(ctx,label,width) {
  ctx.lineWidth = 1.0;
  ctx.textAlign = "right";
  ctx.textBaseline = "top";
  ctx.font = "normal 18px sans-serif";
  ctx.fillStyle = "#000000";
  ctx.beginPath();
  ctx.fillText(label,width-5,5);
  ctx.closePath();
  }


///
///   Routine to select current element for drawing
///
function pickElem(elem) {

  var tablesize = element(1,"max");
  var i, str, mystyle;
  var mode;
  var param = parameters();
  var backcolor = "silver";
  var active = "lightskyblue";

  // If first time routine called, set defaults
  if ( typeof pickElem.metals == 'undefined' ) {
    pickElem.metals = "none";
    pickElem.myfont = "14px";
    if (document.getElementById('pchooser') )
      document.getElementById('pchooser').innerHTML = "Metals";
    }

  // Change display of periodic table
  if (elem == "PView") {
    if (document.getElementById('pchooser') ) {
      if ( document.getElementById('pchooser').innerHTML == "Metals" ) {
          pickElem.metals = "table-cell";
          pickElem.myfont = "10px";
          document.getElementById('pchooser').innerHTML = "Organic";
        } else {
          pickElem.metals = "none";
          pickElem.myfont = "14px";
          document.getElementById('pchooser').innerHTML = "Metals";
        }
      }
    }

  // Turn off display for metals
//  if (elem == "MOff") {
//    pickElem.metals = "none";
//    pickElem.myfont = "14px";
//    if (document.getElementById('MOn') )
//      document.getElementById('MOn').style.color  = "navy";
//    if (document.getElementById('MOff') )
//      document.getElementById('MOff').style.color = "antiquewhite";
//    if (document.getElementById('pchooser') )
//      document.getElementById('pchooser').innerHTML = "Metals";
//    }

  // Turn on display for metals
//  if (elem == "MOn") {
//    pickElem.metals = "table-cell";
//    pickElem.myfont = "10px";
//    if (document.getElementById('pchooser') )
//      document.getElementById('pchooser').innerHTML = "Organic";
//    }

  // Set display options depending on selected view
  if (document.getElementById('Row1') )
      document.getElementById('Row1').style.display   = pickElem.metals;
  if (document.getElementById('Row2') )
      document.getElementById('Row2').style.display   = pickElem.metals;
  if (document.getElementById('Row3') )
      document.getElementById('Row3').style.display   = pickElem.metals;
  if (document.getElementById('RowLa') )
      document.getElementById('RowLa').style.display  = pickElem.metals;
  if (document.getElementById('RowAc') )
      document.getElementById('RowAc').style.display  = pickElem.metals;
  if (document.getElementById('RowLa2') )
      document.getElementById('RowLa2').style.display = pickElem.metals;
  if (document.getElementById('RowAc2') )
      document.getElementById('RowAc2').style.display = pickElem.metals;
//  if (document.getElementById('Mon') )
//      document.getElementById('MOn').style.fontSize   = pickElem.myfont;
//  if (document.getElementById('Moff') )
//      document.getElementById('MOff').style.fontSize  = pickElem.myfont;

  // Loop over all elements in table
  for (i=1; i<tablesize; i++) {
    delete mystyle;
    // Process Main Group elements
    str = "m" + element(i,"symbol");
    if (document.getElementById(str)) {
      mystyle = document.getElementById(str).style;
      }
    // Process metallic elements (not Main Group)
    str = "p" + element(i,"symbol");
    if (document.getElementById(str)) {
      mystyle = document.getElementById(str).style;
      mystyle.display = pickElem.metals;
      }
    // Set display parameters for all elements
    if ( mystyle ) {
      mystyle.backgroundColor = backcolor;
      mystyle.fontSize = pickElem.myfont;
      if (element(i,"symbol") == elem)
        mystyle.backgroundColor = active;
      }
    }

  // Set display parameters for all buttons
  buttonColor("delbtn",0);
  buttonColor("delbond",0);
  buttonColor("rotbond",0);
  if (elem == "Delete") {
    buttonColor("delbtn",1);
    param.atommode="Delete";
    return;
    }
  if (elem == "DelBond") {
    buttonColor("delbond",1);
    param.bondmode="Delete";
    return;
    }
  if (elem == "RotateBond") {
    if (  param.bondmode != "Rotate" ) {
        buttonColor("rotbond",1);
        param.bondmode="Rotate";
      } else {
        param.bondmode="";
        BondRotation("Clear");
      }
    return;
    }

  // Not a button, so set element
  param.element = elem;
  param.atommode = "Add";
  param.bondmode = "Add";

  // Finished with pickElem routine
  }


///
///   Routine to select hybridization pattern for current element
///   Possible values are 1 to 4
///
function pickClouds(hybrid) {
  var i, str;
  var clouds = parseInt(hybrid);
  var param = parameters();

  for (i=1; i<5; i++) {
    str = "cld" + i;
    buttonColor(str,0);
    if (i == clouds) {
      buttonColor(str,1);
      }
    }
  param.clouds = clouds;
  }


//#   function drawmode()
//#
//#   Routine to enable display of "draw mode" interface.
//#
function drawmode() {
  var param = parameters();
  if ( document.getElementById("drawDiv") )
    document.getElementById("drawDiv").style.display = "inline";
  if ( document.getElementById("viewDiv") )
    document.getElementById("viewDiv").style.display = "none";
  buttonColor("modeDraw",1);
  buttonColor("modeView",0);
  param.mode = "Draw";
  param.element = "C";
  param.atommode  = "Add";
  param.bondmode = "Add";
  }


//#   function viewmode()
//#
//#   Routine to enable display of "view mode" interface.
//#
function viewmode() {
  var param = parameters();
  if ( document.getElementById("drawDiv") )
    document.getElementById("drawDiv").style.display = "none";
  if ( document.getElementById("viewDiv") )
    document.getElementById("viewDiv").style.display = "inline";
  buttonColor("modeDraw",0);
  buttonColor("modeView",1);
  param.mode = "View";
  pickElem("ClearBond");

  // Show molecular formula
  formula();
  showCoord(1);
  }


///
///   Routine to allow rotation about a bond
///
///   mode: "Set" sets atoms, "Rotate" performs rotation, or "Clear"
///   values: Two atoms of bond  OR  single rotation angle
///
function BondRotation(mode,value1,value2) {

  // Define local variables
  var i, pos;
  var x, y, xc, yc;
  var cosA, sinA;
  var step=60.0;  // Larger values make more sensitive
  var molecule = Mol();

  // Save two atoms used to define bond rotation
  if ( typeof BondRotation.RotateAtom1 == 'undefined' )
    BondRotation.RotateAtom1 = 0;
  if ( typeof BondRotation.RotateAtom2 == 'undefined' )
    BondRotation.RotateAtom2 = 0;

  // Save list of atoms to rotate if rotation about a bond
  if ( typeof BondRotation.RotateList == 'undefined' ) {
    BondRotation.RotateList = new Array();
    BondRotation.RotateList[0] = 0;
    }

  // If mode is "Clear", reset variables
  if ( mode == "Clear" ) {
    BondRotation.RotateAtom1 = 0;
    BondRotation.RotateAtom2 = 0;
    BondRotation.RotateList[0] = 0;
    return;
    }

  // If mode is "Set", align molecule along bond
  if ( mode == "Set" ) {
    BondRotation.RotateAtom1 = value1;
    BondRotation.RotateAtom2 = value2;
    bondAlign(value1,value2);
    return;
    }

  // If mode is "Rotate", perform rotation
  if ( mode == "Rotate" ) {
    atom1 = BondRotation.RotateAtom1;
    atom2 = BondRotation.RotateAtom2;
    cosA = Math.cos(value1*step*Math.PI/360);
    sinA = Math.sin(value1*step*Math.PI/360);
    if (BondRotation.RotateList[0] == 0) {
      BondRotation.RotateList[0] = 1;
      BondRotation.RotateList[1] = BondRotation.RotateAtom2;
      BondRotation.RotateList = rotlist(BondRotation.RotateList, atom1, atom2);
      }

InfoWin("\n--- Bond rotation ---\n");
for(i=1;i<=BondRotation.RotateList[0];i++){
 j=BondRotation.RotateList[i];
 InfoWin(element(molecule[j].atomicnumber,"symbol")+j+"\n");
 }

    xc = molecule[atom1].x;
    yc = molecule[atom1].y;
    for (pos=1; pos <= BondRotation.RotateList[0]; pos++) {
      i = BondRotation.RotateList[pos];
      x = molecule[i].x - xc;
      y = molecule[i].y - yc;
      molecule[i].x =  cosA*x + sinA*y + xc;
      molecule[i].y = -sinA*x + cosA*y + yc;
      }
    }

  // End of BondRotation routine
  }


///
///   This routine aligns molecule so that bond is parallel to z-axis
///
function bondAlign(atom1, atom2) {
  var i;
  var x, y, z;
  var dx, dy, dz;
  var ctx, cty, stx, sty;
  var molecule = Mol();

  // Determine elements of rotation matrix used to align bond
  dx = molecule[atom2].x - molecule[atom1].x;
  dy = molecule[atom2].y - molecule[atom1].y;
  dz = molecule[atom2].z - molecule[atom1].z;
  if ( (dy == 0) && (dz == 0) ) {
      ctx = 1.0;
      stx = 0.0;
    } else {
      ctx = Math.sqrt( dz*dz / ((dy*dy)+(dz*dz)) );
      stx = Math.sqrt( 1 - (ctx*ctx) );
    }
  vsign = dy*dz;
  if (vsign < 0.0)
    stx = -stx;
  z = stx*dy + ctx*dz;
  if ( (dx == 0) && (z == 0) ) {
      cty = 1.0;
      sty = 0.0;
    } else {
      cty = Math.sqrt( z*z / ((dx*dx)+(z*z)) );
      sty = Math.sqrt( 1 - (cty*cty) );
    }
  vsign = dx*z;
  if (vsign < 0.0)
    sty = -sty;

  // Rotate molecule
  for (i=1; i <= molecule[0].numatoms; i++) {
    x = molecule[i].x;
    y = molecule[i].y;
    z = molecule[i].z;
    molecule[i].x = (x*cty) - (y*stx*sty) - (z*ctx*sty);
    molecule[i].y =           (y*ctx)     - (z*stx);
    molecule[i].z = (x*sty) + (y*stx*cty) + (z*ctx*cty);
    }

  // Make sure second atom in front
  if ( molecule[atom1].z < molecule[atom2].z ) {
    for (i=1; i <= molecule[0].numatoms; i++) {
      molecule[i].x = -molecule[i].x;
      molecule[i].z = -molecule[i].z;
      }
    }

  // End of rotateBond routine
  }


///
///   Routine to determine which atoms bonded to atom2,
///   after but not including atom1
///
function rotlist(RList, atom1, atom2) {
  // Declare local variables
  var i, j;
  var atm, found;
  var molecule = Mol();
  var bonds = BondMatrix();

  // Loop over all bonds on atom2
  for (atm=1; atm <= molecule[0].numatoms; atm++) {
    if ( bonds[atom2][atm] > 0) {
      found = 0;
      if ( atm == atom1 )
        found = 1;
      for (j=1; j <= RList[0]; j++) {
        if ( atm == RList[j] ) {
          found = 1;
          j = RList[0] + 1;
          }
        }
      if (found == 0) {
        RList[0]++;
        RList[RList[0]] = atm;
        rotlist(RList, atom2, atm);
        }
      }
    }

  // End of rotlist routine
  return RList;
  }



// -------------------- Section to handle Reading Files --------------------

///
///   Routine to get filename of local input file from user
///
function readfile(localfile) {
//      console.log(localfile);
      var fr = new FileReader();
      fr.onload = function(fh) {
        validExtension = 0;
        var ext = extension(localfile.name);
        // Read contents and split data into lines
        var contents = fh.target.result;
        var lines = contents.split("\n");

        if ( ext == "xyz" ) {
          validExtension = 1;
          readXYZfile(lines);
          }
        if ( ext == "mol" ) {
          validExtension = 1;
          readMOLfile(localfile,lines);
          }
        if ( ext == "inp" ) {
          validExtension = 1;
          readINPfile(localfile,lines);
          }
        if ( ext == "cif" ) {
          validExtension = 1;
          readCIFfile(localfile,lines);
          }
         if ( ext == "res" ) {
          validExtension = 1;
          readRESfile(localfile,lines);
          }
        if ( ext == "ins" ) {
          validExtension = 1;
          readRESfile(localfile,lines);
          }
        if ( ext == "pdb" ) {
            validExtension = 1;
            readPDBfile(localfile,lines);
            }
        if ( validExtension == 0 ) {
          InfoWin("*** ERROR: Invalid file type for "+localfile.name+". ***",1);
          return;
          }
        centerMolecule();
        drawMolecule();
        }
      fr.readAsText(localfile);
}

function MyFileReader(evt) {
  var validExtension;
  var localfile = evt.target.files[0];
//  console.log("localfile", localfile)
  // Call routine to read and process data
  if (localfile) {
      readfile(localfile);
    } else {
      alert("Failed to load file");
    }
  }


///
///   Routine to determine extension for filename
///
function extension(myfilename) {
  var extension = myfilename.substring(myfilename.lastIndexOf('.')+1);
  return extension.toLowerCase();
  }


//#
//#   function showgallery(title,base,List,Desc,size)
//#
//#   Routine to display multiple files stored on the web server.
//#
//#   Parameters:
//#      title: Title to display before gallery
//#             (If title = "delete", clear gallery)
//#      base:  Path to directory (relative to web root) containing images
//#      List:  Array containing a list of filenames (including extensions)
//#      Desc:  Array containing descriptions for each file
//#      size:  integer width (in px) for each frame
//#
  function showgallery(title,base,List,Desc,size) {

    // Declare local variables
    var i, start, pos;
    var html;
    var frame, canvas;
    var framestr, canvasstr;
    var csize;

    // If title = "delete", clear gallery
    if ( title == "delete" ) {
      if ( typeof showgallery.num != "undefined" ) {
        showgallery.num = 0;
        delete showgallery.list;
        }
      return;
      }

    // If no gallery division present, exit
    if ( ! document.getElementById("gallery") ) {
      alert("Warning: showgallery called, but no <div id=\"gallery\"></div> exists on html page.");
      return;
      }

    // Set up storage to keep track of all files to load in all galleries
    if ( typeof showgallery.list === "undefined" ) {
      showgallery.num = 0;
      showgallery.list = [];
      }
    start = showgallery.num;

    // Define base names to use for each frame and canvas
    canvas = "gallerycanvas";
    frame = "galleryframe";

    // Add files to list for display in all galleries
    pos = start;
    for (i=0; i < List.length; i++) {
      showgallery.list[pos] = base + List[i];
      showgallery.num++;
      pos++;
      }

    // Set dimension for canvas
    csize = "width=\"" + size + "\" height=\"" + size + "\"></canvas>";

    // Create content and add to web page
    html = "";
    if ( title ) {
      html = "<h3>" + title + "</h3>\n";
      }
    pos = start;
    for (i=0; i < List.length; i++) {
      canvasstr = canvas + pos;
      framestr  = frame + pos;
      html += "<div class=\"galleryframe\" id=\"" + framestr + "\">";
      html += "<canvas id=\"" + canvasstr + "\" " + csize + "\n";
      html += "<p style=\"text-align: center;\">";
      html += Desc[i];
      html += "</p></div>\n";
      pos++;
      }
    html += "<p class=\"clear\">&nbsp;</p>\n\n";
    document.getElementById("gallery").innerHTML += html;

    // If debug window exists, write output to this window
    if ( document.getElementById("debug") ) {
      document.getElementById("debug").innerHTML += html;
      }

    // Set correct size for each box
    px = size + "px";
    pos = start;
    for (i=0; i < List.length; i++) {
      framestr = frame + pos;
      if ( document.getElementById(framestr) )
        document.getElementById(framestr).style.width = px;
      pos++;
      }

    // Updating HTML appears to erase old molecules, so load all molecules in list
    for (i=0; i < showgallery.num; i++) {
      canvasstr = canvas + i;
      activeWin(canvasstr);
      delMolecule();
      readServerFile(showgallery.list[i]);
      if ( document.getElementById("debug") ) {
        html  = "\n\nProcessed molecule "+i;
        html += " named "+showgallery.list[i];
        document.getElementById("debug").innerHTML += html;
        }
      }

    }


//#
//#   function galleryUniform()
//#
//#   Routine to force all molecules that are part of a "gallery" to be displayed with the same size scale.
//#
function galleryUniform() {

  // Declare local variables
  var i, num, scale;
  var framestr;
  var frame = "gallerycanvas";
  var molecule = [];

  // Find number of gallery images on page
  num = 0;
  framestr = frame + num;
  while ( document.getElementById(framestr) ) {
    num++;
    framestr = frame + num;
    }

  // Find scale factor for largest molecule
  scale = 1000;
  for (i=0; i < num; i++) {
    framestr = frame + i;
    activeWin(framestr);
    molecule = Mol();
    if ( molecule[0].AtomScale < scale ) {
      scale = molecule[0].AtomScale;
      }
    }

  // Scale molecules
  if ( scale < 1000.0 ) {
    for (i=0; i < num; i++) {
      framestr = frame + i;
      activeWin(framestr);
      molecule = Mol();
      molecule[0].AtomScale = scale;
      drawMolecule();
      }
    }
  }


//#
//#   function galleryReset()
//#
//#   For molecules that are part of a "gallery", this routine optimizes the size of each molecule individually.
//#
function galleryReset() {

  // Declare local variables
  var i, num;
  var framestr;
  var frame = "gallerycanvas";

  // Find number of gallery images on page
  num = 0;
  framestr = frame + num;
  while ( document.getElementById(framestr) ) {
    num++;
    framestr = frame + num;
    }

  // Reset view for each molecule
  for (i=0; i < num; i++) {
    framestr = frame + i;
    activeWin(framestr);
    centerMolecule();
    drawMolecule();
    }
  }


//#
//#   function readServerFile(filename)
//#
//#   Routine to read contents of file stored on the web server.
//#
//#   Parameter:
//#      filename:  Name (URL) of file (including path)
//#

function readwebview(ext, lines) {
//  console.log(ext, lines);
  // Call routine to read and process data
  validExtension = 0;
  if ( ext == "xyz" ) {
     validExtension = 1;
     readXYZfile(ext, lines);
     }
  if ( ext == "mol" ) {
     validExtension = 1;
     readMOLfile(ext, lines);
     }
  if ( ext == "inp" ) {
     validExtension = 1;
     readINPfile(ext, lines);
     }
  if ( ext == "cif" ) {
     validExtension = 1;
     readCIFfile(ext, lines);
     }
  if ( ext == "res" ) {
     validExtension = 1;
     readRESfile(ext, lines);
     }
  if ( ext == "ins" ) {
     validExtension = 1;
     readRESfile(ext, lines);
     }
  if ( ext == "pdb" ) {
      validExtension = 1;
      readPDBfile(localfile,lines);
      }
  if ( validExtension == 0 ) {
    InfoWin("*** ERROR: Invalid file type. ***",1);
    return;
    }

  // Update display
  centerMolecule();
  drawMolecule();
  }


function readServerFile(filename) {
//  console.log(filename);
  // Define local variables
  var lines;
  var validExtension;
  var fileinfo = new Array();
  var ext = extension(filename);
  var xmlhttp;

  // Use XML to get contents of file from "server"
  xmlhttp=new XMLHttpRequest();
  xmlhttp.open('GET', filename, false);
  xmlhttp.send();
  lines = xmlhttp.responseText.split('\n');

  // Call routine to read and process data
  validExtension = 0;
  if ( ext == "xyz" ) {
     validExtension = 1;
     readXYZfile(lines);
     }
  if ( ext == "mol" ) {
     validExtension = 1;
     readMOLfile(localfile,lines);
     }
  if ( ext == "inp" ) {
     validExtension = 1;
     readINPfile(localfile,lines);
     }
  if ( ext == "cif" ) {
     validExtension = 1;
     readCIFfile(lines);
     }
  if ( validExtension == 0 ) {
    InfoWin("*** ERROR: Invalid file type. ***",1);
    return;
    }

  // Update display
  centerMolecule();
  drawMolecule();
  }


//#
//#   function InfoWin(mytext,mode)
//#
//#   Routine to write text to information window (textarea with an id of "information").
//#
//#   Parameters:
//#     mytext:  String to write to output window
//#     mode:    If >0, then clear text window
//#
function InfoWin(mytext,mode) {
  var outstring = mytext || "";
  var clearwin = mode || 0;

  if ( ! document.getElementById("information") )
    return;
  if ( clearwin > 0 )
    document.getElementById("information").value  = outstring;
  else
    document.getElementById("information").value += outstring;
  }


//#   function loadMolecule()
//#
//#   Routine to load molecular information for methane molecule.
//#
function loadMolecule() {

  // Add atomic coordinates to molecule array
  addAtom(6,  0.000,  0.000,  0.000);
  addAtom(1,  0.874,  0.618,  0.000);
  addAtom(1, -0.874,  0.618,  0.000);
  addAtom(1,  0.000, -0.618,  0.874);
  addAtom(1,  0.000, -0.618, -0.874);
  // Add bonds to bond array
  addBond(1, 2);
  addBond(1, 3);
  addBond(1, 4);
  addBond(1, 5);
  }


//#   function resetView()
//#
//#   Routine to reset view. Center, rescale, and remove highlights.
//#
function resetView() {

  // Define local variables
  var i;
  var molecule = Mol();

  // Remove highlights and show all atoms
  for ( i=1; i <= molecule[0].numatoms; i++ ) {
    molecule[i].highlite = 0;
    molecule[i].hide = 0;
    }

  // Clear Information Window
  InfoWin("",1);

  // Formula, center, scale, and draw
  formula();
  centerMolecule();
  drawMolecule();
  }


//#   function buttonColor(button, mode)
//#
//#   Set color of buttons
//#
//#   Parameters
//#     button - string containing ID name for button
//#     mode   - 0=inactive, 1=active
//#
function buttonColor(button, mode) {

  mode = mode || 0;
  var buttoncolor = "silver";
  if ( mode )
    buttoncolor = "lightskyblue";
  if ( document.getElementById(button) )
    document.getElementById(button).style.backgroundColor = buttoncolor;
  }


//#   function initialize()
//#
//#   Initialization Routines
//#     - Load properties of elements
//#     - Define Handlers for mouse events
//#     - Draw molecule
//#
//function loadfromfile(url, name){
//      var req = new XMLHttpRequest();
//      req.open('GET', url, true);
//      //alert(req.responseText);
//      req.setRequestHeader('Content-Type', 'text/plain');
//      req.onreadystatechange = function (aEvt) {
//        if (req.readyState == 4) {
//          if(req.status == 200) {
//            var content = req.responseText.split("\n")
//             readCIFfile(url, content);
////            readfile(localfile);
//            centerMolecule();
//            drawMolecule();
//          } else {
//            console.log("Error fetching " + url);
//          }
//        }
//      };
//      req.send(null);
//    }

function initwebview(ext, data) {
  if (data) {
      // Define handler for drawing area (canvas)
      // activeWin defines routines to handle mouse events
      var activeCanvas = activeWin();
      // If no canvas element found, see if userDefined() creates one.
      if ( ! activeCanvas ) {
        userDefined();
        activeCanvas = activeWin("");
        if ( ! activeCanvas ) {
          alert("No canvas present. Either create a canvas or remove onLoad=initialize() statement from <body>.");
          }
        return;
        }
      // if ( molfile && molfile!=undefined) {
      //   // Verify browser supports HTML5 FileReader
      //   if (window.File && window.FileReader && window.FileList && window.Blob) {
      //       molfile.addEventListener('change', MyFileReader, false);
      //     } else {
      //       alert('The File APIs are not fully supported by your browser.');
      //     }
      //   }  
      if ( molfile ) {
        // Verify browser supports HTML5 FileReader
        if (window.File && window.FileReader && window.FileList && window.Blob) {
            molfile.addEventListener('change', MyFileReader, false);
          } else {
            alert('The File APIs are not fully supported by your browser.');
          }
        }
      readwebview(ext, data);
      //console.log(data);
      // Create periodic table
      drawPeriodic();
      // Initialize molecular geometry
      var molecule = Mol();
      // Set display mode to View
      viewmode();
      }

//      else {
//        delMolecule();
//      if (molecule[0].numatoms < 1) {
//        delMolecule();
//        loadMolecule();
//        formula();  // Display molecular formula
//        centerMolecule();  // Center molecule
//        }
//       drawMolecule();
//      // Set default drawing atom
//      pickClouds(4);
//      pickElem("C");
//
//      // Execute user-defined routine
//      //userDefined();
  }

function initialize() {

  // Define handler for drawing area (canvas)
  // activeWin defines routines to handle mouse events
  var activeCanvas = activeWin();
  var molfile = document.getElementById('molfile');
  // If no canvas element found, see if userDefined() creates one.
  if ( ! activeCanvas ) {
    userDefined();
    activeCanvas = activeWin("");
    if ( ! activeCanvas ) {
      alert("No canvas present. Either create a canvas or remove onLoad=initialize() statement from <body>.");
      }
    return;
    }

  // Handler for loading files. After file selected, calls "MyFileReader"
  if ( molfile ) {
    // Verify browser supports HTML5 FileReader
    if (window.File && window.FileReader && window.FileList && window.Blob) {
        molfile.addEventListener('change', MyFileReader, false);
      } else {
        alert('The File APIs are not fully supported by your browser.');
      }
    }

  // Create periodic table
  drawPeriodic();

  // Initialize molecular geometry
  var molecule = Mol();

  // Set display mode to View
  viewmode();

  // Draw molecule
  if ( typeof molecule == 'undefined' )
    delMolecule();
  if (molecule[0].numatoms < 1) {
    delMolecule();
    loadMolecule();
    formula();  // Display molecular formula
    centerMolecule();  // Center molecule
    }
   drawMolecule();

  // Set default drawing atom
  pickClouds(4);
  pickElem("C");

  // Execute user-defined routine
  //userDefined();
  }
// -------------------- build.js file --------------------

///
///   Routine to add/change atoms and add H
///
function newAtom(OnAtom) {

  // Declare local variables
  var i, j, k, numbonds;
  var vx, vy, vz, vd;
  var Rij, Rnew;
  var elem, pos;
  var errorH;
  var bondlist = [];
  var param = parameters();
  var molecule = Mol();
  var bonds = BondMatrix();
  var activeCanvas = activeWin("");

  // Lookup information for current element 
  atomicNumber = lookupSymbol(param.element);

  // Set number of bonds on selected atom
  numbonds = bonds[OnAtom][0];

  //
  // If number of bonds == 0, arbitrarily add new atom along
  // x axis and attach the appropriate number of hydrogen atoms.
  //
  if (numbonds == 0) {
    Rnew = element(atomicNumber,"radius") + element(molecule[OnAtom].atomicnumber,"radius");
    dx = molecule[OnAtom].x + Rnew;
    dy = molecule[OnAtom].y;
    dz = molecule[OnAtom].z;
    addAtom(atomicNumber, dx, dy, dz);
    addBond(OnAtom,molecule[0].numatoms);
    addH(molecule[0].numatoms);
    centerMolecule();
    drawMolecule(activeCanvas);
    return;
    }

  // Create list of atoms bonded to current atom
  pos = 0;
  for (i=1; i <= molecule[0].numatoms; i++) {
    if ( (bonds[OnAtom][i] > 0) && (i != OnAtom))
      bondlist[++pos] = i;
    }
  bondlist[0] = pos;
  if ( bondlist[0] != bonds[OnAtom][0])
    alert("ERROR: Supposed to be "+numbonds+" bonds on atom "+OnAtom+", but "+pos+" bonds found.");

  // If atom to add is H, add one H
  if (atomicNumber == 1) {
    vx = 0.0;
    vy = 0.0;
    vz = 0.0;
    for (i=1; i <= numbonds; i++) {
      j = bondlist[i];
      dx = molecule[j].x - molecule[OnAtom].x;
      dy = molecule[j].y - molecule[OnAtom].y;
      dz = molecule[j].z - molecule[OnAtom].z;
      dd = Math.sqrt(dx*dx+dy*dy+dz*dz);
      vx += dx/dd;
      vy += dy/dd;
      vz += dz/dd;
      }
    vd = Math.sqrt(vx*vx+vy*vy+vz*vz);
    Rnew = element(1,"radius") + element(molecule[OnAtom].atomicnumber,"radius");
    vx = molecule[OnAtom].x - vx*Rnew/vd;
    vy = molecule[OnAtom].y - vy*Rnew/vd;
    vz = molecule[OnAtom].z - vz*Rnew/vd;
    addAtom(1, vx, vy, vz);
    // Check to be sure new H atom not too close to other bonded atoms
    for (pos=1; pos <= numbonds; pos++) {
      errorH = 0;
      Rij = distance(molecule,bondlist[pos],molecule[0].numatoms);
      if ( Rij < 0.2 )
        errorH = 1;
      }
    if ( (errorH)  &&  (numbonds>1) ) {
    // If bonded atoms all close to a plane, place H above/below plane
      i = bondlist[1];
      j = bondlist[2];
      vx  = (molecule[i].y-molecule[OnAtom].y) * (molecule[j].z-molecule[OnAtom].z);
      vx -= (molecule[i].z-molecule[OnAtom].z) * (molecule[j].y-molecule[OnAtom].y);
      vy  = (molecule[i].z-molecule[OnAtom].z) * (molecule[j].x-molecule[OnAtom].x);
      vy -= (molecule[i].x-molecule[OnAtom].x) * (molecule[j].z-molecule[OnAtom].z);
      vz  = (molecule[i].x-molecule[OnAtom].x) * (molecule[j].y-molecule[OnAtom].y);
      vz -= (molecule[i].y-molecule[OnAtom].y) * (molecule[j].x-molecule[OnAtom].x);
      vd = Math.sqrt(vx*vx+vy*vy+vz*vz);
      molecule[molecule[0].numatoms].x = molecule[OnAtom].x - vx*Rnew/vd;
      molecule[molecule[0].numatoms].y = molecule[OnAtom].y - vy*Rnew/vd;
      molecule[molecule[0].numatoms].z = molecule[OnAtom].z - vz*Rnew/vd;
      errorH = 0;
      for (pos=1; pos <= numbonds; pos++) {
        Rij = distance(molecule,bondlist[pos],molecule[0].numatoms);
        if ( Rij < 0.2 )
          errorH = 1;
        }
      }
    if ( errorH ) {
      alert("Error adding H atom");
      delAtom(molecule[0].numatoms);
      return;
      }

    // If no errors, continue
    addBond(OnAtom,molecule[0].numatoms);
    centerMolecule();
    drawMolecule(activeCanvas);
    numbonds = 0;
    return;
    }

  //
  // If number of bonds == 1, change to new atom type,
  // change bond length, and add appropriate # of H.
  //
  if (numbonds == 1) {
    i = OnAtom;
    j =bondlist[1];
    dx = molecule[i].x - molecule[j].x;
    dy = molecule[i].y - molecule[j].y;
    dz = molecule[i].z - molecule[j].z;
    Rij = Math.sqrt(dx*dx+dy*dy+dz*dz);
    Rnew = element(atomicNumber,"radius") + element(molecule[j].atomicnumber,"radius");
    dx *= Rnew/Rij;
    dy *= Rnew/Rij;
    dz *= Rnew/Rij;
    molecule[i].atomicnumber = atomicNumber;
    molecule[i].x = dx + molecule[j].x;
    molecule[i].y = dy + molecule[j].y;
    molecule[i].z = dz + molecule[j].z;
    addH(OnAtom);
    centerMolecule();
    drawMolecule(activeCanvas);
    }

  // If number of bonds > 1, then simply change atom type
  if (numbonds > 1) {
    molecule[OnAtom].atomicnumber = atomicNumber;
    drawMolecule(activeCanvas);
    }

  // Finished with newAtom routine
  }


///
///   Routine to add H atoms to 'atom'
///
function addH(atom) {

  var i, j, clouds, Z, numH;
  var atom1, atom2;
  var errmsg;
  var param = parameters();
  var molecule = Mol();
  var bonds = BondMatrix();
  var activeCanvas = activeWin("");

  // Only automatically add H atoms to p-block elements
  if ( element(molecule[atom].atomicnumber,"block") != "p" )
    return;

  // Determine how many H atoms to add
  clouds = param.clouds;
  Z = molecule[atom].atomicnumber;
  valence = element(Z,"valence");
  numH = 3 + clouds - valence;
  if (numH < 1)
    clouds = 1;
  if ( clouds <= 1 )
    return;

  // Find first atom bonded to current atom
  atom1 = 0;
  i = 0;
  while ( (atom1==0) && (i < molecule[0].numatoms) ) {
    i++;
    if ( (bonds[atom][i]>0) && (i != atom) )
      atom1 = i;
    }

  // Find first atom bonded to atom1
  atom2 = 0;
  if ( atom1 ) {
    i = 0;
    while ( (atom2==0) && (i < molecule[0].numatoms) ) {
      i++;
      if ( bonds[atom1][i]>0 )
        if ( (i != atom) && (i != atom1) )
          atom2 = i;
      }
    }

  // Call appropriate routines to add hydrogen atom(s)
  switch (clouds) {
    case 2:
          add1H(atom,atom1);
          break;
    case 3:
          add2H(atom,atom1,atom2,numH);
          break;
    case 4:
          add3H(atom,atom1,atom2,numH);
          break;
    default:
          break;
    }

  // Draw molecule
  centerMolecule();
  drawMolecule(activeCanvas);

  // Finished
  }


///
///   Routine to add one H atom to sp hybridized atom
///
function add1H(atom,i) {

  // Declare local variables
  var j, dx, dy, dz;
  var Za, Rai, RH;
  var Hx, Hy, Hz;
  var molecule = Mol();

  // Calculate H--atom bond length
  Za = molecule[atom].atomicnumber;
  RH = element(Za,"radius") + element(1,"radius");

  // If atom has zero bonds, add H along x-axis
  if (i == 0) {
    dx = molecule[atom].x + RH;
    dy = molecule[atom].y;
    dz = molecule[atom].z;
    addAtom(1, Hx, Hy, Hz);
    addBond(atom,molecule[0].numatoms);
    return;
    }

  // Calculate vector atom->i
  dx = molecule[i].x - molecule[atom].x;
  dy = molecule[i].y - molecule[atom].y;
  dz = molecule[i].z - molecule[atom].z;
  Rai = Math.sqrt(dx*dx+dy*dy+dz*dz);

  // Calculate position of new H
  Hx = molecule[atom].x - dx*RH/Rai;
  Hy = molecule[atom].y - dy*RH/Rai;
  Hz = molecule[atom].z - dz*RH/Rai;
  addAtom(1, Hx, Hy, Hz);
  addBond(atom,molecule[0].numatoms);

  // End add1H routine
  }


///
///   Routine to add up to 2 H atoms to sp2 hybridized atom
///
function add2H(atom,i,j,numH) {
  // Declare local variables
  var Za, Zi, Zj, RaH;
  var daiX, daiY, daiZ, Rai;
  var dijX, dijY, dijZ, Rij, ang;
  var dpX, dpY, dpZ, dpd;
  var Hx, Hy, Hz, dHx, dHy, dHz;
  var LX, LY, LZ, Lscale;
  var base;
  var aug = new Array();
  var molecule = Mol();

  // Lookup atomic numbers and calculate X-H Bond length
  Za = molecule[atom].atomicnumber;
  RaH = element(Za,"radius") + element(1,"radius");

  // If atom contains zero bonds, add 2H in xy plane
  if (i == 0) {
    Hx = molecule[atom].x + 0.5*RaH;
    Hy = molecule[atom].y + RaH*Math.sqrt(3)/2;
    Hz = molecule[atom].z;
    addAtom(1, Hx, Hy, Hz);
    addBond(atom,molecule[0].numatoms);
    if (numH > 1) {
      Hy = molecule[atom].y - RaH*Math.sqrt(3)/2;
      addAtom(1, Hx, Hy, Hz);
      addBond(atom,molecule[0].numatoms);
      }
    return;
    }

  // Lookup atomic numbers for first bonded atom
  Zi = molecule[i].atomicnumber;
  daiX = molecule[i].x - molecule[atom].x;
  daiY = molecule[i].y - molecule[atom].y;
  daiZ = molecule[i].z - molecule[atom].z;
  Rai = Math.sqrt(daiX*daiX + daiY*daiY + daiZ*daiZ);

  // If atom contains only one bond, pick arbitrary atom for second point
  if (j == 0) {
    for (var ii=1; ii<molecule[0].numatoms; ii++) {
      if ( (ii!=atom) && (ii!=i) ) {
        j = ii;
        ii = molecule[0].numatoms;
        }
      }
    }

  // If molecule contains only two atoms, shift all atoms to xy plane
  if (j == 0) {
    molecule[atom].x = 0.0;
    molecule[atom].y = 0.0;
    molecule[atom].z = 0.0;
    molecule[i].x = -Rai;
    molecule[i].y = 0.0;
    molecule[i].z = 0.0;
    Hx = molecule[atom].x + 0.5*RaH;
    Hy = molecule[atom].y + RaH*Math.sqrt(3)/2;
    Hz = molecule[atom].z;
    addAtom(1, Hx, Hy, Hz);
    addBond(atom,molecule[0].numatoms);
    if (numH > 1) {
      Hy = molecule[atom].y - RaH*Math.sqrt(3)/2;
      addAtom(1, Hx, Hy, Hz);
      addBond(atom,molecule[0].numatoms);
      }
    return;
    }

  // Lookup atomic numbers for second bonded atom
  Zj = molecule[j].atomicnumber;
  dijX = molecule[j].x - molecule[i].x;
  dijY = molecule[j].y - molecule[i].y;
  dijZ = molecule[j].z - molecule[i].z;
  Rij = Math.sqrt(dijX*dijX + dijY*dijY + dijZ*dijZ);

  // ----- Add first H -----
  // Dot-product of HA*Ai
  aug[0] = daiX;
  aug[1] = daiY;
  aug[2] = daiZ;
  aug[3] = -RaH*Rai/2;

  // Dot-product of HA*ij
  ang = (-daiX*dijX-daiY*dijY-daiZ*dijZ)/(Rai*Rij);
  ang = Math.acos(-1/2) + Math.PI - Math.acos(ang);
  aug[4] = dijX;
  aug[5] = dijY;
  aug[6] = dijZ;
  aug[7] = RaH*Rij*Math.cos(ang);

  // Calculate cross product (ji x ai)
  dpX =  dijZ*daiY - dijY*daiZ;
  dpY =  dijX*daiZ - dijZ*daiX;
  dpZ =  dijY*daiX - dijX*daiY;
  dpd = Math.sqrt(dpX*dpX+dpY*dpY+dpZ*dpZ);

  // Dot-product of HA * ( ji X ai )
  aug[8] = dpX;
  aug[9] = dpY;
  aug[10] = dpZ;
  aug[11] = 0.0;

  // Calculate coordinates of H1
  var coord = gaussElim(aug);
  Hx = molecule[atom].x + coord[0];
  Hy = molecule[atom].y + coord[1];
  Hz = molecule[atom].z + coord[2];
  addAtom(1, Hx, Hy, Hz);
  addBond(atom,molecule[0].numatoms);

  // ----- Add second H -----
  if (numH == 1) {
    return;
    }

  // Dot-product of HA*Ai
  aug[0] = daiX;
  aug[1] = daiY;
  aug[2] = daiZ;
  aug[3] = -RaH*Rai/2;

  // Dot-product of HA*ij
  ang = (-daiX*dijX-daiY*dijY-daiZ*dijZ)/(Rai*Rij);
  ang = Math.acos(ang) - Math.acos(0.5);
  aug[4] = dijX;
  aug[5] = dijY;
  aug[6] = dijZ;
  aug[7] = RaH*Rij*Math.cos(ang);

  // Dot-product of LH2* (iA x ij)
  aug[8]  = dpX;
  aug[9]  = dpY;
  aug[10] = dpZ;
  aug[11] = 0.0;

  // Calculate coordinates for H2
debug  = "\nRow 1: "+aug[0].toFixed(4)+" "+aug[1].toFixed(4);
debug += " "+aug[2].toFixed(4)+" "+aug[3].toFixed(4);
debug += "\nRow 2: "+aug[4].toFixed(4)+" "+aug[5].toFixed(4);
debug += " "+aug[6].toFixed(4)+" "+aug[7].toFixed(4);
debug += "\nRow 3: "+aug[8].toFixed(4)+" "+aug[9].toFixed(4);
debug += " "+aug[10].toFixed(4)+" "+aug[11].toFixed(4);
  coord = gaussElim(aug);
  Hx = molecule[atom].x + coord[0];
  Hy = molecule[atom].y + coord[1];
  Hz = molecule[atom].z + coord[2];
debug = "H2 at: ("+Hx.toFixed(4)+", "+Hy.toFixed(4)+", "+Hz.toFixed(4)+")";
  addAtom(1, Hx, Hy, Hz);
  addBond(atom,molecule[0].numatoms);

debug  = "atom = "+atom+"  i = "+i+"  numatoms = "+molecule[0].numatoms;
debug += "\n"+element(molecule[molecule[0].numatoms].atomicnumber,"symbol");
debug += "\nRow 1: "+aug[0].toFixed(4)+" "+aug[1].toFixed(4);
debug += " "+aug[2].toFixed(4)+" "+aug[3].toFixed(4);
debug += "\nRow 2: "+aug[4].toFixed(4)+" "+aug[5].toFixed(4);
debug += " "+aug[6].toFixed(4)+" "+aug[7].toFixed(4);
debug += "\nRow 3: "+aug[8].toFixed(4)+" "+aug[9].toFixed(4);
debug += " "+aug[10].toFixed(4)+" "+aug[11].toFixed(4);
debug += "\nCross: "+dpX.toFixed(4)+" "+dpY.toFixed(4)+" "+dpZ.toFixed(4);
//alert(debug);

  // End of add2H routine
  }


///
///   Routine to add H atoms to sp3 hybridized atom
///
function add3H(atom,i,j,numH) {
  // Declare local variables
  var Za, Zi, Zj, RaH;
  var daiX, daiY, daiZ, Rai;
  var dijX, dijY, dijZ, Rij, ang;
  var dpX, dpY, dpZ, dpd;
  var Hx, Hy, Hz, dHx, dHy, dHz;
  var LX, LY, LZ, Lscale;
  var base;
  var aug = new Array();
  var molecule = Mol();

  // Lookup atomic numbers and calculate X-H Bond length
  Za = molecule[atom].atomicnumber;
  Zi = molecule[i].atomicnumber;
  Zj = molecule[j].atomicnumber;
  RaH = element(Za,"radius") + element(1,"radius");

  // ----- Add first H -----

  // Dot-product of HA*Ai
  daiX = molecule[i].x - molecule[atom].x;
  daiY = molecule[i].y - molecule[atom].y;
  daiZ = molecule[i].z - molecule[atom].z;
  Rai = Math.sqrt(daiX*daiX + daiY*daiY + daiZ*daiZ);
  aug[0] = daiX;
  aug[1] = daiY;
  aug[2] = daiZ;
  aug[3] = -RaH*Rai/3;

  // Dot-product of HA*ij
  dijX = molecule[j].x - molecule[i].x;
  dijY = molecule[j].y - molecule[i].y;
  dijZ = molecule[j].z - molecule[i].z;
  Rij = Math.sqrt(dijX*dijX + dijY*dijY + dijZ*dijZ);
  ang = (-daiX*dijX-daiY*dijY-daiZ*dijZ)/(Rai*Rij);
  ang = Math.acos(-1/3) + Math.PI - Math.acos(ang);
  aug[4] = dijX;
  aug[5] = dijY;
  aug[6] = dijZ;
  aug[7] = RaH*Rij*Math.cos(ang);

  // Cross-product ji X ai
  dpX =  dijZ*daiY - dijY*daiZ;
  dpY =  dijX*daiZ - dijZ*daiX;
  dpZ =  dijY*daiX - dijX*daiY;
  dpd = Math.sqrt(dpX*dpX+dpY*dpY+dpZ*dpZ);
  // Handle special case where j=0 and i located at (0,0,0)
  if (dpd == 0) {
    dpX =  molecule[atom].y;
    dpY = -molecule[atom].x;
    dpZ =  molecule[atom].z;
    dpd = Math.sqrt(dpX*dpX+dpY*dpY+dpZ*dpZ);
    }

  // Dot-product of HA * ( ji X ai )
  aug[8] = dpX;
  aug[9] = dpY;
  aug[10] = dpZ;
  aug[11] = 0.0;

  var coord = gaussElim(aug);
  Hx = molecule[atom].x + coord[0];
  Hy = molecule[atom].y + coord[1];
  Hz = molecule[atom].z + coord[2];
  addAtom(1, Hx, Hy, Hz);
  addBond(atom,molecule[0].numatoms);

  // ----- Add second H -----
  if (numH == 1) {
    return;
    }

  // Create point L
  base = molecule[0].numatoms;
  Lscale = RaH/(Rai*3);
  LX = molecule[atom].x - daiX*Lscale;
  LY = molecule[atom].y - daiY*Lscale;
  LZ = molecule[atom].z - daiZ*Lscale;

  // Dot-product of LH2*LH
  aug[0] = molecule[base].x - LX;
  aug[1] = molecule[base].y - LY;
  aug[2] = molecule[base].z - LZ;
  aug[3] = -RaH*RaH*4/9;

  // Dot-product of LH2*LA
  dHx = coord[0];
  dHy = coord[1];
  dHz = coord[2];
  aug[4] = molecule[atom].x - LX;
  aug[5] = molecule[atom].y - LY;
  aug[6] = molecule[atom].z - LZ;
  aug[7] = 0.0;

  // Dot-product of LH2* (iA x ij)
  aug[8]  = dpX;
  aug[9]  = dpY;
  aug[10] = dpZ;
  aug[11] = RaH*dpd*Math.sqrt(2/3);

  // Calculate coordinates for H2
  coord = gaussElim(aug);
  Hx = LX + coord[0];
  Hy = LY + coord[1];
  Hz = LZ + coord[2];
  addAtom(1, Hx, Hy, Hz);
  addBond(atom,molecule[0].numatoms);

  // ----- Add third H -----
  if (numH == 2) {
    return;
    }

  // Dot-product of LH2*LH
  aug[0] = molecule[base].x - LX;
  aug[1] = molecule[base].y - LY;
  aug[2] = molecule[base].z - LZ;
  aug[3] = -RaH*RaH*4/9;

  // Dot-product of LH2*LA
  dHx = coord[0];
  dHy = coord[1];
  dHz = coord[2];
  aug[4] = molecule[atom].x - LX;
  aug[5] = molecule[atom].y - LY;
  aug[6] = molecule[atom].z - LZ;
  aug[7] = 0.0;

  // Dot-product of LH2* (iA x ij)
  dpd = Math.sqrt(dpX*dpX+dpY*dpY+dpZ*dpZ);
  aug[8]  = dpX;
  aug[9]  = dpY;
  aug[10] = dpZ;
  aug[11] = -RaH*dpd*Math.sqrt(2/3);
debug  = "atom = "+atom+"  i = "+i+"  numatoms = "+molecule[0].numatoms;
debug += "\n"+element(molecule[molecule[0].numatoms].atomicnumber,"symbol");
debug += "\nRow 1: "+aug[0].toFixed(4)+" "+aug[1].toFixed(4);
debug += " "+aug[2].toFixed(4)+" "+aug[3].toFixed(4);
debug += "\nRow 2: "+aug[4].toFixed(4)+" "+aug[5].toFixed(4);
debug += " "+aug[6].toFixed(4)+" "+aug[7].toFixed(4);
debug += "\nRow 3: "+aug[8].toFixed(4)+" "+aug[9].toFixed(4);
debug += " "+aug[10].toFixed(4)+" "+aug[11].toFixed(4);
debug += "\nCross: "+dpX.toFixed(4)+" "+dpY.toFixed(4)+" "+dpZ.toFixed(4);
//alert(debug);

  // Calculate coordinates for H3
  coord = gaussElim(aug);
//  Hx = molecule[atom].x + coord[0];
//  Hy = molecule[atom].y + coord[1];
//  Hz = molecule[atom].z + coord[2];
  Hx = LX + coord[0];
  Hy = LY + coord[1];
  Hz = LZ + coord[2];
  addAtom(1, Hx, Hy, Hz);
  addBond(atom,molecule[0].numatoms);

  // End of add3H routine
  }


///
///   Use gaussian elimination to solve for new coordinates.
///   Argument is augmented matrix of the form:
///     | ax  ay  az  =  ac |
///     | bx  by  bz  =  bc |
///     | cx  cy  cz  =  cc |
///
///   Returns a matrix containing the solution (x,y,z)
///
function gaussElim(aug) {
//  var aug = [2, -2, 0, -6, 1, -1, 1, 1, 0, 3, -2, -5];
//  var aug = [1, -2, 1, 0, 2, 1, -3, 5, 4, -7, 1, -1];
  var x, y, z, c;
  var coord = new Array();

  var ax = parseFloat(aug[0]);
  var ay = parseFloat(aug[1]);
  var az = parseFloat(aug[2]);
  var ac = parseFloat(aug[3]);
  var bx = parseFloat(aug[4]);
  var by = parseFloat(aug[5]);
  var bz = parseFloat(aug[6]);
  var bc = parseFloat(aug[7]);
  var cx = parseFloat(aug[8]);
  var cy = parseFloat(aug[9]);
  var cz = parseFloat(aug[10]);
  var cc = parseFloat(aug[11]);

//alert("| "+ax.toFixed(4)+" "+ay.toFixed(4)+" "+az.toFixed(4)+" = "+ac.toFixed(4)+" |\n"+
//      "| "+bx.toFixed(4)+" "+by.toFixed(4)+" "+bz.toFixed(4)+" = "+bc.toFixed(4)+" |\n"+
//      "| "+cx.toFixed(4)+" "+cy.toFixed(4)+" "+cz.toFixed(4)+" = "+cc.toFixed(4)+" |\n");

  // Swap rows to place largest X variable in first row
  if ( (Math.abs(bx) > Math.abs(ax))  &&  (Math.abs(bx) > Math.abs(cx)) ) {
  	 x=ax;  y=ay;  z=az;  c=ac;
  	 ax=bx; ay=by; az=bz; ac=bc;
  	 bx=x;  by=y;  bz=z;  bc=c;
    }

  if ( (Math.abs(cx) > Math.abs(ax))  &&  (Math.abs(cx) > Math.abs(bx)) ) {
  	 x=ax;  y=ay;  z=az;  c=ac;
  	 ax=cx; ay=cy; az=cz; ac=cc;
  	 cx=x;  cy=y;  cz=z;  cc=c;
    }

  if ( Math.abs(cx) > Math.abs(bx) ) {
    x=bx;  y=by;  z=bz;  c=bc;
  	 bx=cx; by=cy; bz=cz; bc=cc;
  	 cx=x;  cy=y;  cz=z;  cc=c;
    }

  // Add rows to "zero-out" first column
  if ( (ax != 0)  && (bx != 0 ) ) {
    factor = -ax/bx;
    bx = 0.0;
    by = by*factor + ay;
    bz = bz*factor + az;
    bc = bc*factor + ac;
    }
  if ( (ax != 0)  && (cx != 0 ) ) {
    factor = -ax/cx;
    cx = 0.0;
    cy = cy*factor + ay;
    cz = cz*factor + az;
    cc = cc*factor + ac;
    }

  // Swap rows to place largest Y variable in second row
  if (Math.abs(cy) > Math.abs(by)) {
    y=by;  z=bz;  c=bc;
    by=cy; bz=cz; bc=cc;
    cy=y;  cz=z;  cc=c;
    }

  // Add rows to "zero-out" second column
  if ( (by != 0)  && (cy != 0 ) ) {
    factor = -by/cy;
    cy = 0.0;
    cz = cz*factor + bz;
    cc = cc*factor + bc;
    }

//alert("| "+ax.toFixed(4)+" "+ay.toFixed(4)+" "+az.toFixed(4)+" = "+ac.toFixed(4)+" |\n"+
//      "| "+bx.toFixed(4)+" "+by.toFixed(4)+" "+bz.toFixed(4)+" = "+bc.toFixed(4)+" |\n"+
//      "| "+cx.toFixed(4)+" "+cy.toFixed(4)+" "+cz.toFixed(4)+" = "+cc.toFixed(4)+" |\n");

  // Solve
  coord[2] = 0.0;
  if (cz != 0) {
    coord[2] = cc/cz;
    }
  coord[1] = 0.0;
  if (by != 0) {
    coord[1] = (bc-(bz*coord[2]))/by;
    }
  coord[0] = 0.0;
  if (ax != 0) {
    coord[0] = (ac - (az*coord[2]) - (ay*coord[1]))/ax;
    }
//alert("dx = "+coord[0].toFixed(4)+", dy = "+coord[1].toFixed(4)+", dz = "+coord[2].toFixed(4));

  // Return answer
  return coord;
  }
//
// -------------------- mechanics.js --------------------
//

//#   function mechanics()
//#
//#   Simple routine to perform crude optimization of structure.
//#
function mechanics() {

  // Define local variables
  var i, j, k;
  var Z;
  var loop;
  var erg, deltaE;
  var molOLD = new Array();
  var molNEW = new Array();
  var molecule = Mol();
  // Drawing Canvas info
  var activecanvas = activeWin("");
  var canvas = document.getElementById(activecanvas);
  var ctx = canvas.getContext('2d');
  var width = canvas.width;
  // Parameters
  var MAXSTEP=0.2;
  var MAXLOOP=500;
  var ETHRESH = 0.0000002;

  // Save Molecular information
  Undo("save");

  // Clear information window
  InfoWin("Simple Geometry Optimization starting\n",1);
  geomLabel(ctx,"Simple Geometry Optimization started",width);

  // Determine hybridization of all atoms in molecule
  molOLD = hybridization();
  var DEBUG=0;  // Debug hybridization routine
  if (DEBUG > 0) {
    InfoWin("Hybridization\n");
    for (i=1; i <= molecule[0].numatoms; i++) {
      Z = molecule[i].atomicnumber;
      InfoWin(element(Z,"symbol")+" has "+molOLD[i].hybrid+" hybrid orbitals\n");
      }
    }

  // Calculate energy of initial geometry
  erg = mechEnergy(molOLD);
  molOLD[0].energy = erg;
  molOLD[0].step = MAXSTEP;

  // Populate molNEW array
  molNEW[0] = new energyObject();
  molNEW[0].energy = molOLD[0].energy;
  molNEW[0].step = molOLD[0].step;
  for (i=1; i <= molecule[0].numatoms; i++) {
    molNEW[i] = new mechanicsObject();
    molNEW[i].hybrid = molOLD[i].hybrid;
    molNEW[i].x = molOLD[i].x;
    molNEW[i].y = molOLD[i].y;
    molNEW[i].z = molOLD[i].z;
    }

  // Call routine to calculate new geometry
  loop = 0;
  deltaE = ETHRESH*2.0;
  InfoWin(0+": Energy = "+erg.toFixed(8)+"\n");
  while ( (loop<MAXLOOP) && (deltaE>ETHRESH) ) {
    molNEW = optimize(molOLD);
    deltaE = Math.abs( molOLD[0].energy - molNEW[0].energy );

    // Don't allow step size to increase too much
    if ( molNEW[0].step > MAXSTEP )
      molNEW[0].step = MAXSTEP;

    // Copy values from molNEW array into molOLD
    molOLD[0].energy = molNEW[0].energy;
    molOLD[0].step = molNEW[0].step;
    for (i=1; i <= molecule[0].numatoms; i++) {
      molOLD[i].hybrid = molNEW[i].hybrid;
      molOLD[i].x = molNEW[i].x;
      molOLD[i].y = molNEW[i].y;
      molOLD[i].z = molNEW[i].z;
      }

    // Force at least 3 iterations
    loop++;
    if (loop < 3)
      if ( deltaE < ETHRESH )
        deltaE = ETHRESH*2.0;

    // If structure approaching convergence, increase step size
    if ( deltaE < ETHRESH ) {
      if ( molNEW[0].step < MAXSTEP ) {
        molOLD[0].step *= 1.5;
        molNEW = optimize(molOLD);
        deltaE = Math.abs( molOLD[0].energy - molNEW[0].energy );
        if ( deltaE > ETHRESH ) {
          molOLD[0].energy = molNEW[0].energy;
          molOLD[0].step = molNEW[0].step;
          for (i=1; i <= molecule[0].numatoms; i++) {
            molOLD[i].hybrid = molNEW[i].hybrid;
            molOLD[i].x = molNEW[i].x;
            molOLD[i].y = molNEW[i].y;
            molOLD[i].z = molNEW[i].z;
            }
          }
        }
      }

    // Save current structure and display geometry every 5 steps
    InfoWin(loop+": Energy = "+molNEW[0].energy.toFixed(8)+"\n");
    //InfoWin(" Step = "+molNEW[0].step.toFixed(5)+"\n");
    DEBUG=1;
    if ( (DEBUG>0) && (loop%5 == 0) ) {
      for (i=1; i <= molecule[0].numatoms; i++) {
        molecule[i].x = molNEW[i].x;
        molecule[i].y = molNEW[i].y;
        molecule[i].z = molNEW[i].z;
        }
      centerMolecule();
      drawMolecule();
      geomLabel(ctx,"Simple Geometry Optimization in progress.",width);
      }
    }

  // Save optimized coordinates and display structure
  InfoWin("Final Energy at loop "+loop+" = "+molNEW[0].energy.toFixed(8)+"\n");
  InfoWin("Geometry Optimization complete.\n");
  if ( loop >= MAXLOOP )
    InfoWin("Too many steps. Optimization may not be complete.\n");
  for (i=1; i <= molecule[0].numatoms; i++) {
    molecule[i].x = molNEW[i].x;
    molecule[i].y = molNEW[i].y;
    molecule[i].z = molNEW[i].z;
    }
  centerMolecule();
  drawMolecule();

  // Finished with mechanics routine
  }


///
///   Define object to hold temporary molecular information
///
function mechanicsObject() {
  this.hybrid = 0;
  this.x = 0.0;
  this.y = 0.0;
  this.z = 0.0;
  }


///
///   Define object to hold temporary energy/optimization information
///
function energyObject() {
  this.energy = 0.0;
  this.rstep = 0;
  this.astep = 0;
  }


//#   function distance(mol, atomA, atomB)
//#
//#   Calculate the distance between two atoms in mol array.
//#
function distance(mol, atomA, atomB) {

  // Calculate distance between atoms
  var dx = mol[atomA].x - mol[atomB].x;
  var dy = mol[atomA].y - mol[atomB].y;
  var dz = mol[atomA].z - mol[atomB].z;
  var r = Math.sqrt(dx*dx+dy*dy+dz*dz);

  // Exit distance routine
  return r;
  }


//#   function angle(mol, atomA, atomB, atomC)
//#
//#   Calculate the angle between A--B--C in mol array
//#
function angle(mol, atomA, atomB, atomC) {

  // Calculate vector BA
  var dax = mol[atomA].x - mol[atomB].x;
  var day = mol[atomA].y - mol[atomB].y;
  var daz = mol[atomA].z - mol[atomB].z;
  var ra = Math.sqrt(dax*dax+day*day+daz*daz);

  // Calculate vector BC
  var dbx = mol[atomC].x - mol[atomB].x;
  var dby = mol[atomC].y - mol[atomB].y;
  var dbz = mol[atomC].z - mol[atomB].z;
  var rb = Math.sqrt(dbx*dbx+dby*dby+dbz*dbz);

  // Calculate bond angle
  var ang = (dax*dbx + day*dby + daz*dbz) / (ra*rb);
  if (ang >  1.0) ang = 1.0;
  if (ang < -1.0) ang = -1.0;
  ang = Math.acos(ang) * 180.0 / Math.PI;

  // Exit distance routine
  return ang;
  }


//#   function dihedral(mol, atomA, atomB, atomC, atomD)
//#
//#   Routine to calculate the dihedral angle for A--B--C--D
//#
function dihedral(mol, atomA, atomB, atomC, atomD) {

  // Define local variables
  var i, j, k;
  var dux, duy, duz;
  var dvx, dvy, dvz;
  var crossA, crossAx, crossAy, crossAz;
  var crossB, crossBx, crossBy, crossBz;

  // Calculate cross product of BA x BC
  dux = mol[atomA].x - mol[atomB].x;
  duy = mol[atomA].y - mol[atomB].y;
  duz = mol[atomA].z - mol[atomB].z;
  dvx = mol[atomC].x - mol[atomB].x;
  dvy = mol[atomC].y - mol[atomB].y;
  dvz = mol[atomC].z - mol[atomB].z;
  crossAx = duy*dvz - duz*dvy;
  crossAy = duz*dvx - dux*dvz;
  crossAz = dux*dvy - duy*dvx;
  crossA  = Math.sqrt(crossAx*crossAx + crossAy*crossAy + crossAz*crossAz);

  // Calculate cross product of CD x CB
  dux = mol[atomD].x - mol[atomC].x;
  duy = mol[atomD].y - mol[atomC].y;
  duz = mol[atomD].z - mol[atomC].z;
  crossBx = duz*dvy - duy*dvz;
  crossBy = dux*dvz - duz*dvx;
  crossBz = duy*dvx - dux*dvy;
  crossB  = Math.sqrt(crossBx*crossBx + crossBy*crossBy + crossBz*crossBz);

  // Use dot product to calculate dihedral angle
  ang = (-crossAx*crossBx-crossAy*crossBy-crossAz*crossBz)/(crossA*crossB);
  if (ang >  1.0) ang = 1.0;
  if (ang < -1.0) ang = -1.0;
  ang = Math.acos(ang) * 180.0 / Math.PI;

  // Finished with dihedral routine
  return ang;
  }


///
///   Determine number of hybrid orbitals on all atoms
///
function hybridization() {

  // Define local variables
  var i, j, k;
  var valence;
  var optmol = new Array();
  var molecule = Mol();
  var bonds = BondMatrix();

  // Copy molecule data into local array
  optmol[0] = new energyObject();
  optmol[0].energy = 0.0;
  optmol[0].step = 0.0;
  for (i=1; i <= molecule[0].numatoms; i++) {
    optmol[i] = new mechanicsObject();
    optmol[i].hybrid = 0;
    optmol[i].x = molecule[i].x;
    optmol[i].y = molecule[i].y;
    optmol[i].z = molecule[i].z;
    }

  // Loop over all atoms in molecule
  for (i=1; i <= molecule[0].numatoms; i++) {
    valence = element(molecule[i].atomicnumber,"valence");
    switch (valence) {
      case 1:
      case 2:
      case 3:
          optmol[i].hybrid = bonds[i][0];
          break;
      default:
          optmol[i].hybrid = valence + bonds[i][0] - 4;
          break;
      }
    while ( (optmol[i].hybrid>bonds[i][0]) && (optmol[i].hybrid>=5) ) {
      optmol[i].hybrid = optmol[i].hybrid-1;
      }
    }

  // Look for delocalized lone pairs
  for (i=1; i <= molecule[0].numatoms; i++) {
    if ( (optmol[i].hybrid == 4) && (bonds[i][0]<4) ) {
      for (j=1; j <= molecule[0].numatoms; j++) {
        k = bonds[i][j];
        if (k > 0) {
          if ( optmol[k].hybrid == 3 ) {
            optmol[i].hybrid = 3;
            // InfoWin("Delocalized lone pair found on atom "+i+" bonded to "+bonds[i][j]+"\n");
            }
          }
        }
      }
    }

  // End hybridization routine
  return optmol;
  }


///
///   Calculate the mechanics energy of the current geometry
///
function mechEnergy(current) {

  // Define local variables
  var i, j, k;
  var ii, bi, bj, ia, ja;
  var r0, r1, r2;
  var dx, dy, dz, r, dr;
  var atomA, atomB, maxBonds;
  var da, dax, day, daz;
  var db, dbx, dby, dbz;
  var ang;
  var tetra = Math.acos(-1/3.0) * 180.0 / Math.PI;
  var energy = 0.0;
  var molecule = Mol();
  var bonds = BondMatrix();

  // Parameters
  var penaltyR  = 20000.0;
  var penaltyA  =    10.0;
  var penaltyD  =     5.0;
  var penaltyVDW =  500.0;

  // Look for hybridization error
  DEBUG=1;
  if ( DEBUG > 0 ) {
    var hytotal = 0;
    for (i=1; i <= molecule[0].numatoms; i++) {
      hytotal += current[i].hybrid;
      }
    if (hytotal < molecule[0].numatoms)
      InfoWin("*** Too few hybrid orbitals ("+hytotal+") returned at end of optimize\n");
    }

  // Calculate energy penalty for bond lengths
  for (i=1; i <= molecule[0].numatoms; i++) {
    r1 = element(molecule[i].atomicnumber,"radius");
    if ( current[i].hybrid == 3 )
      r1 -= 0.05;
    if ( current[i].hybrid == 2 )
      r1 -= 0.10;
    for (j=1; j <= molecule[0].numatoms; j++) {
      if ( bonds[i][j] > 0) {
        k = j;
        r2 = element(molecule[k].atomicnumber,"radius");
        if ( current[k].hybrid == 3 )
          r2 -= 0.05;
        if ( current[k].hybrid == 2 )
          r2 -= 0.10;
        r0 = r1 + r2;  // Ideal bond length
        dx = current[i].x - current[k].x;
        dy = current[i].y - current[k].y;
        dz = current[i].z - current[k].z;
        r = Math.sqrt(dx*dx+dy*dy+dz*dz);
        energy += penaltyR*(r-r0)*(r-r0);
        }
      }
    }

  // Calculate energy penalty for bond angles
  for (i=1; i <= molecule[0].numatoms; i++) {
    if (current[i].hybrid > 1) {
      for (j=1; j < molecule[0].numatoms; j++) {
        if (bonds[i][j] > 0) {
          atomA = j;
          dax = current[atomA].x  - current[i].x;
          day = current[atomA].y  - current[i].y;
          daz = current[atomA].z  - current[i].z;
          da = Math.sqrt(dax*dax + day*day + daz*daz);
          for (k=j+1; k <= molecule[0].numatoms; k++) {
          	if (bonds[i][k] > 0) {
              atomB = k;
              dbx = current[atomB].x  - current[i].x;
              dby = current[atomB].y  - current[i].y;
              dbz = current[atomB].z  - current[i].z;
              db = Math.sqrt(dbx*dbx + dby*dby + dbz*dbz);
              ang = (dax*dbx+day*dby+daz*dbz)/(da*db);
              if (ang >  1.0) ang = 1.0;
              if (ang < -1.0) ang = -1.0;
              ang = Math.acos(ang) * 180.0 / Math.PI;
              switch (current[i].hybrid) {
                case 2:
                    energy += penaltyA*(ang-180.0)*(ang-180.0);
                    break;
                case 3:
                    energy += penaltyA*(ang-120.0)*(ang-120.0);
                    break;
                case 4:
                    energy += penaltyA*(ang-tetra)*(ang-tetra);
                    break;
                case 5:
                case 6:
                    if (ang < 100.0)
                      energy += penaltyA*(ang-90.0)*(ang-90.0);
                    break;
                }
          	  }
            }
          }
        }
      }
    }

  // Calculate energy penalty for sp3-sp3 dihedral angles
  for (i=1; i < molecule[0].numatoms; i++) {
    if (current[i].hybrid == 4) {
      for (ii=i+1; ii<=molecule[0].numatoms; ii++) {
        if ( (bonds[i][ii] > 0) && (current[ii].hybrid == 4) ) {
          j = ii;
          for (bi=1; bi<=molecule[0].numatoms; bi++) {
            if ( (bonds[i][bi]>0) && (bi!=j) && (bi!=i) ) {
              ia = bi;
              for (bj=1; bj<=molecule[j].numatoms; bj++) {
                if ( (bonds[j][bj]>0) && (bj!=j) && (bj!=i) && (bj!=ia) ) {
                  ja = molecule[j].bonds[bj];
                  ang = Math.abs(dihedral(current, ia, i, j, ja));
                  while (ang > 120.0)
                    ang -= 120.0;
                  energy += penaltyD*(ang-60.0)*(ang-60.0);
//                  InfoWin("Dihedral: "+ia+"-"+i+"-"+j+"-"+ja);
//                  InfoWin(" = "+ang+"\n");
                  }
                }
              }
            }
          }
        }
      }
    }

  // Calculate energy penalty for sp2-sp2 dihedral angles (pi bonds)
  for (i=1; i < molecule[0].numatoms; i++) {
    if (current[i].hybrid == 3) {
      for (ii=i+1; ii<=molecule[i].numatoms; ii++) {
        if ( (bonds[i][ii]>0) && (current[j].hybrid == 3) ) {
          j = ii;
          for (bi=1; bi<=molecule[i].numatoms; bi++) {
            if ( (bonds[i][bi]>0) && (bi!=j) && (bi!=i) ) {
              ia = bi;
              for (bj=1; bj<=molecule[j].numatoms; bj++) {
                if ( (bonds[j][bj]>0) && (bj!=i) && (bj!=j) && (bj!=ia)  ) {
                  ja = bj;
                  ang = Math.abs(dihedral(current, ia, i, j, ja));
                  if (ang > 180.0)
                    ang -= 180.0;
                  if (ang > 135.0)
                    ang = 180.0 - ang;
                  energy += penaltyD*ang*ang;
                  // InfoWin("Dihedral: "+ia+"-"+i+"-"+j+"-"+ja);
                  // InfoWin(" = "+ang+"\n");
                  }
                }
              }
            }
          }
        }
      }
    }

  // Calculate energy penalty for van der Waal's repulsion
  for (i=1; i < molecule[0].numatoms; i++) {
    r1 = element(molecule[i].atomicnumber,"radius");
    for (j=i+1; j <= molecule[0].numatoms; j++) {
      r2 = element(molecule[j].atomicnumber,"radius");
      r = distance(current, i, j);
      if ( r < 0.1 )
        r = 0.1;
      r = r/(r1+r2);
      energy += penaltyVDW / (r*r*r*r*r*r);
      }
    }

  // End of mechEnergy routine
  return energy;
  }


///
///   Calculate 'optimal' change in all coordinates
///
function changexyz(current) {

  // Define local variables
  var molecule = Mol();
  var i, j, k;
  var ixyz;
  var delta = [];
  var EZero, energyX, energyY, energyZ;
  var stepx, stepy, stepz;
  var stepfactor;
  var oldx, oldy, oldz;
  var randomnumber;

  // Parameters
  var stepsize = current[0].step;

  // Debug hybridization routine
  var DEBUG=0;
  if (DEBUG > 0) {
    InfoWin("Hybridization\n");
    for (i=1; i <= molecule[0].numatoms; i++) {
      Z = molecule[i].atomicnumber;
      InfoWin(element(Z,"symbol")+" has "+current[i].hybrid+" hybrid orbitals\n");
      }
    }

  // Initialize delta array
  for (i=0; i <= molecule[0].numatoms; i++) {
    delta[i] = [0.0, 0.0, 0.0];
    }

  // Populate trial array
  var trial = new Array();
  trial[0] = new energyObject();
  trial[0].energy = current[0].energy;
  trial[0].step = current[0].step;
  for (i=1; i <= molecule[0].numatoms; i++) {
    trial[i] = new mechanicsObject();
    trial[i].hybrid = current[i].hybrid;
    trial[i].x = current[i].x;
    trial[i].y = current[i].y;
    trial[i].z = current[i].z;
    }

  // Loop over all coordinates, looking for 'best' changes
  EZero = mechEnergy(trial);
  for (i=1; i <= molecule[0].numatoms; i++) {

    // Save current coordinates
    oldx = trial[i].x;
    oldy = trial[i].y;
    oldz = trial[i].z;

    // Loop over changes in all coordinates
    for (ixyz=0; ixyz<6; ixyz++) {
      stepx = 0.0;
      stepy = 0.0;
      stepz = 0.0;
      energyX = EZero;
      energyY = EZero;
      energyZ = EZero;
      (ixyz%2) ? stepfactor=1.0 : stepfactor=-1.0;
      switch (ixyz) {
        case 0:
        case 1:
            trial[i].x = oldx + stepfactor*stepsize;
            Energy = mechEnergy(trial);
            while ( (Energy>EZero) && (stepfactor>0.1) ) {
              stepfactor *= 0.75;
              trial[i].x = oldx + stepfactor*stepsize;
              Energy = mechEnergy(trial);
              }
            if ( Energy < energyX )
              stepx = stepfactor;
            trial[i].x = oldx;
            delta[i][0] = stepx*stepsize;
            break;
        case 2:
        case 3:
            trial[i].y = oldy + stepfactor*stepsize;
            Energy = mechEnergy(trial);
            while ( (Energy>EZero) && (stepfactor>0.1) ) {
              stepfactor *= 0.75;
              trial[i].y = oldy + stepfactor*stepsize;
              Energy = mechEnergy(trial);
              }
            if ( Energy < energyY )
              stepy = stepfactor;
            trial[i].y = oldy;
            delta[i][1] = stepy*stepsize;
            break;
        case 4:
        case 5:
            trial[i].z = oldz + stepfactor*stepsize;
            Energy = mechEnergy(trial);
            while ( (Energy>EZero) && (stepfactor>0.1) ) {
              stepfactor *= 0.75;
              trial[i].z = oldz + stepfactor*stepsize;
              Energy = mechEnergy(trial);
              }
            if ( Energy < energyZ )
              stepz = stepfactor;
            trial[i].z = oldz;
            delta[i][2] = stepz*stepsize;
            break;
        }
      }

    // Finished loop for atom 'i'
    }

  // End of changexyz routine
  return delta;
  }


///
///   Simple molecular mechanics (kind of) geometry optimization
///
function optimize(current) {

  // Define local variables
  var i, j, k;
  var ib;
  var newstep;
  var EFit;
  var EMin;
  var beststep, trial;
  var maxstep;
  var delta  = new Array();
  var molNEW  = new Array();
  var molecule = Mol();

  // Parameters
  var MINSTEP=0.001;
  var step = current[0].step;
  var eINITIAL = current[0].energy;

  // Look for a few obvious errors
  DEBUG=1;
  if ( DEBUG > 0 ) {
    var erg = mechEnergy(current);
    if (erg != eINITIAL)
      InfoWin("*** Call to mechEnergy changed energy from "+eINITIAL+" to "+erg+"\n");
    var hytotal = 0;
    for (i=1; i <= molecule[0].numatoms; i++) {
      hytotal += current[i].hybrid;
      }
    if (hytotal < molecule[0].numatoms)
      InfoWin("*** Too few hybrid orbitals ("+hytotal+")\n");
    }

  // Initialize delta array
  for (i=0; i <= molecule[0].numatoms; i++) {
    delta[i] = [0.0, 0.0, 0.0];
    }

  // Call routine to calculate changes in coordinates
  // and find maximum change.
  delta = changexyz(current);
  maxstep = 0.0;
  for (i=0; i <= molecule[0].numatoms; i++) {
    for (j=0; j < 3; j++) {
      if ( Math.abs(delta[i][j]) > maxstep )
        maxstep = Math.abs(delta[i][j]);
      }
    }

  // Simple line search to find best change in coordinates
  EMin = current[0].energy;
  beststep = 0.0;
  trial = 1.0;
  EFit = trialEnergy(current,delta,trial);
  while ( (EFit > EMin) && (trial > 0.002) ) {
    trial *= 0.75;
    EFit = trialEnergy(current,delta,trial);
    }
  if (EFit < EMin) {
    beststep = trial;
    EMin = EFit;
    }

  // Determine new step sizes for next iteration
  newstep = (beststep+0.5) * (current[0].step + maxstep);
  if (newstep < MINSTEP)
    newstep = MINSTEP;

  // Populate molNEW object with new geometry
  molNEW[0] = new energyObject();
  molNEW[0].energy = EMin;
  molNEW[0].step = newstep;
  for (i=1; i <= molecule[0].numatoms; i++) {
    molNEW[i] = new mechanicsObject();
    molNEW[i].hybrid = current[i].hybrid;
    molNEW[i].x = current[i].x + beststep*delta[i][0];
    molNEW[i].y = current[i].y + beststep*delta[i][1];
    molNEW[i].z = current[i].z + beststep*delta[i][2];
    }

  // DEBUG: Show changes in coordinates from optimization
  DEBUG = 0;
  if (DEBUG > 0) {
    for (i=0; i <= molecule[0].numatoms; i++) {
      InfoWin("Change in coordinates = (");
      for (j=0; j < 3; j++) {
        InfoWin(delta[i][j].toFixed(5));
        if (j<2)
          InfoWin(", ");
        }
      InfoWin(")\n");
      }
    InfoWin("--- Max change = "+maxstep.toFixed(5)+"\n");
    }

  // Finished with optimize routine
  return (molNEW);
  }


///
///   Calculate the mechanics energy of the current geometry
///
function trialEnergy(current,delta,step) {

  // Define local variables
  var i;
  var trial = new Array();
  var molecule = Mol();

  // Populate array
  trial[0] = new energyObject();
  trial[0].energy = current[0].energy;
  trial[0].step = current[0].step;
  for (i=1; i <= molecule[0].numatoms; i++) {
    trial[i] = new mechanicsObject();
    trial[i].hybrid = current[i].hybrid;
    trial[i].x = current[i].x + step*delta[i][0];
    trial[i].y = current[i].y + step*delta[i][1];
    trial[i].z = current[i].z + step*delta[i][2];
    }

  // End of trialEnergy routine
  return mechEnergy(trial);
  }
