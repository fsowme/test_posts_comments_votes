from rest_framework import serializers


class BaseVoteSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(
        default=serializers.CurrentUserDefault(),
        slug_field="id",
        read_only=True,
    )

    class Meta:
        fields = "__all__"
        extra_kwargs = {
            "vote_type": {"required": True},
        }
