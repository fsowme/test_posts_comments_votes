from rest_framework import serializers


class BaseVoteSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(
        default=serializers.CurrentUserDefault(),
        slug_field="username",
        read_only=True,
    )

    class Meta:
        extra_kwargs = {
            "vote_type": {"required": True},
        }
