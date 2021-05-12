{
  description = "Simulating Chia Plotting";

  inputs = {
    nixpkgs.url = "github:NixOS/nixpkgs/nixos-20.09";
    flake-utils.url = "github:numtide/flake-utils";
  };

  outputs = { self, nixpkgs, flake-utils, ... }: flake-utils.lib.eachSystem [
    "x86_64-linux" "i686-linux" "aarch64-linux"
  ] (system:
    let pkgs = import nixpkgs {
          inherit system;
        };

        chiafan-py-dev = pkgs.python3.withPackages (python-packages: with python-packages;  [
          setuptools
          click
        ]);
    in {
      devShell = pkgs.mkShell rec {
        name = "chiafan-dev";
        buildInputs = with pkgs; [
          chiafan-py-dev
        ];
      };
    });
}
