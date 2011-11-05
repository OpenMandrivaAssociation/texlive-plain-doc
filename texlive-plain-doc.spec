# revision 15878
# category Package
# catalog-ctan /info/plain-doc/csname.txt
# catalog-date 2009-11-09 15:03:08 +0100
# catalog-license noinfo
# catalog-version undef
Name:		texlive-plain-doc
Version:	20091109
Release:	1
Summary:	A list of plain.tex cs names
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/info/plain-doc/csname.txt
License:	NOINFO
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/plain-doc.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/plain-doc.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3

%description
The document constitutes a list of every control sequence name
(csname) described in the TeXbook, together with an indication
of whether the csname is a primitive TeX command, or is defined
in plain.tex.

#-----------------------------------------------------------------------
%files
%doc %{_texmfdistdir}/doc/plain/plain-doc/csname.txt
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar doc %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
