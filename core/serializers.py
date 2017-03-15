from rest_framework import serializers

from . import models


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Comment
        exclude = (
            "expense",
        )
        # fields = "__all__"


class ExpenseSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True)
    user = serializers.CharField(source="user.username")

    class Meta:
        model = models.Expense
        fields = "__all__"




        # To serialize:
        # o = Expense.objects.first()
        # d = ExpenseSerializer(o).data

        # To deserialize:
        # ser = ExpenseSerializer(data=d)
        # if ser.is_valid():
        #     data = ser.validated_data
