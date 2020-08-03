import boto3
import click


def detect(bucket, name):
    client = boto3.client("rekognition")
    print(f"This is the bucket {bucket} and the name {name}")
    response = client.detect_labels(
        Image={"S3Object": {"Bucket": bucket, "Name": name,}}
    )
    return response


@click.command(help="This is a computer vision application.")
@click.option("--name", prompt="I need the image filename", help="Need Image filename")
@click.option("--bucket", prompt="I need the bucketname", help="Bucket")
@click.option("--color", prompt="I need the color", help="This is the color")
def cli(bucket, name, color):
    result = detect(bucket, name)
    click.echo(click.style(f"These are your labels: {result}", fg=color))


if __name__ == "__main__":
    cli()

# print(detect(bucket = "netflix-film-studio-23", name = "dessert.jpg"))
