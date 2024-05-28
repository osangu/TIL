[Automatically Convert](https://github.com/jpadilla/pyjwt/issues/321)

encode시에 datetime으로 넣으면, 자동으로 timestamp로 바꾸어서 넣는다.


잘 봐야 되는 함수들.
- `encode`
    ```python
        def encode(
            self,
            payload: dict[str, Any],
            key: AllowedPrivateKeys | str | bytes,
            algorithm: str | None = "HS256",
            headers: dict[str, Any] | None = None,
            json_encoder: type[json.JSONEncoder] | None = None,
            sort_headers: bool = True,
    ) -> str:
        # Check that we get a dict
        if not isinstance(payload, dict):
            raise TypeError(
                "Expecting a dict object, as JWT only supports "
                "JSON objects as payloads."
            )

        # Payload
        payload = payload.copy()
        for time_claim in ["exp", "iat", "nbf"]:
            # Convert datetime to a intDate value in known time-format claims
            if isinstance(payload.get(time_claim), datetime):
                payload[time_claim] = timegm(payload[time_claim].utctimetuple())
                print(payload[time_claim])

        json_payload = self._encode_payload(
            payload,
            headers=headers,
            json_encoder=json_encoder,
        )

        return api_jws.encode(
            json_payload,
            key,
            algorithm,
            headers,
            json_encoder,
            sort_headers=sort_headers,
        )
    ```
- `_validate_exp`
    ```python
        def _validate_exp(
                self,
                payload: dict[str, Any],
                now: float,
                leeway: float,
        ) -> None:
            try:
                exp = int(payload["exp"])
            except ValueError:
                raise DecodeError("Expiration Time claim (exp) must be an" " integer.")

            print(exp, now, leeway)
            if exp <= (now - leeway):
                raise ExpiredSignatureError("Signature has expired")
    ```