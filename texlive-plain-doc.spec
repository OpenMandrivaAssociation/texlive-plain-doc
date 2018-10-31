Name:		texlive-plain-doc
Version:	20180303
Release:	2
Summary:	A list of plain.tex cs names
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/info/plain-doc/csname.txt
License:	PD
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/plain-doc.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/plain-doc.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg

%description
The document constitutes a list of every control sequence name
(csname) described in the TeXbook, together with an indication
of whether the csname is a primitive TeX command, or is defined
in plain.tex.

#-----------------------------------------------------------------------
%files
%doc %{_texmfdistdir}/doc/plain/plain-doc/csname.txt

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar doc %{buildroot}%{_texmfdistdir}
