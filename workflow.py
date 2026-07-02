import flyte


env = flyte.TaskEnvironment(
	name="addition-workflow",
	image=flyte.Image.from_debian_base(python_version=(3, 12)),
)


def format_message(message: str) -> str:
	return f"ok: {message}"


@env.task
def hello() -> str:
	return format_message("union")


@env.task()
async def main() -> str:
	return hello()
