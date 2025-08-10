export async function getTransactions(limit) {
  const res = await fetch(`http://localhost:8000/transactions?limit=${limit}`);
  if (!res.ok) throw new Error("Error al obtener transacciones");
  return await res.json();
}
