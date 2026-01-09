const userApi = "https://api.example.com/v1/users?id=123&debug=true";
fetch(userApi, {
  headers: { Authorization: "Bearer test-token-abc123" },
});

axios.post("https://api.example.com/v1/admin/impersonate", { userId: 42 });

const ws = new WebSocket("wss://ws.example.com/socket");

const gqlPath = "/graphql";
const apiKey = "apiKey=AKIA_TEST_KEY_1234567890";

