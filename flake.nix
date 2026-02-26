{
  inputs.nixpkgs.url = "github:NixOS/nixpkgs/nixos-unstable";

  outputs = { self, nixpkgs }: let
    pkgs = nixpkgs.legacyPackages.x86_64-linux;
  in {
    devShells.x86_64-linux.default = pkgs.mkShell {
      packages = with pkgs; [
        # C++ build
        cmake
        ninja
        gcc14

        # Python tooling (ghidra scripts, codegen, tests)
        python312
        uv
      ];

      shellHook = ''
        if [ ! -d .venv ]; then
          uv venv
        fi
        source .venv/bin/activate
      '';
    };
  };
}
