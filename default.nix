{ buildPythonApplication, setuptools, click }:

buildPythonApplication rec {
  pname = "chiafan-plot-sim";
  version = "1.0.0";

  src = ./.;

  propagatedBuildInputs = [
    setuptools click
  ];
}
