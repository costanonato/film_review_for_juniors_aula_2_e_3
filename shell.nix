let
  nixpkgs = fetchTarball "https://github.com/NixOS/nixpkgs/tarball/nixos-23.11";
  pkgs = import nixpkgs { config = {}; overlays = []; };
in

pkgs.mkShell {
  packages = [
    pkgs.vscode
    pkgs.git
    pkgs.neofetch
    (pkgs.python3.withPackages (ps: [
      ps.pip
      ps.django
      ps.django-extensions
      ps.djangorestframework
    ])) 
  ];

  shellHook = ''
    source venv/bin/activate
    code .
  '';
}

