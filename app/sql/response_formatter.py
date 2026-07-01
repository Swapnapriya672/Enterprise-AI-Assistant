from app.core.exceptions import SQLException


class SQLResponseFormatter:
    """
    Formats SQL response.
    """

    @staticmethod
    def format(
        rows: list[dict]
    ) -> dict:

        try:

            return {

                "status": "success",

                "total_rows": len(rows),

                "data": rows

            }

        except Exception as exception:

            raise SQLException(
                "Failed to format SQL response."
            ) from exception