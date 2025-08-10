export async function getBalance() {
  const res = await fetch("http://localhost:8000/accounts/balance");
  if (!res.ok) {
    throw new Error("Error al obtener el saldo");
  }
  return await res.json(); 
}
