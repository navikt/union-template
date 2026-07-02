import flyte


env = flyte.TaskEnvironment(
    name="addition-workflow",
    image=flyte.Image.from_debian_base(python_version=(3, 12)),
)


def add_numbers(a: int, b: int) -> int:
    return a + b


@env.task
async def addition_workflow(a: int = 1, b: int = 2) -> int:
    return add_numbers(a=a, b=b)
