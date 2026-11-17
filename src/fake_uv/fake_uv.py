import click


@click.group()
def cmd_group():
    pass


@cmd_group.command()
@click.argument("package")
@click.option("-m", "--with-manager", default="uv")
def add(package, with_manager):
    if with_manager == "uv":
        print(f"Adding and installing {package} using uv...")
    else:
        print("Only uv is supported by this application.")


@cmd_group.command()
@click.argument("package")
@click.option("-m", "--with-manager", default="uv")
def remove(package, with_manager):
    if with_manager == "uv":
        print(f"Removing {package} using uv...")
    else:
        print("Only uv is supported by this application.")


if __name__ == "__main__":
    cmd_group()


# @click.command()
# def operation():
#     @click.argument("package", nargs=1, type=str)
# def adding(package):
#     print(f"Adding and installing {package} ...")
