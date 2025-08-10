export default function TransactionsTable({ transactions }) {
  return (
    <table className="min-w-full bg-white border border-gray-300">
      <thead>
        <tr className="bg-gray-100 border-b">
          <th className="p-2 border">AccountId</th>
          <th className="p-2 border">TransactionId</th>
          <th className="p-2 border">Amount</th>
          <th className="p-2 border">Type</th>
          <th className="p-2 border">CreatedAt</th>
        </tr>
      </thead>
      <tbody>
        {transactions.map((tx) => (
          <tr key={tx.TransactionId} className="hover:bg-gray-50">
            <td className="p-2 border">{tx.AccountId}</td>
            <td className="p-2 border">{tx.TransactionId}</td>
            <td className="p-2 border">${tx.Amount}</td>
            <td className="p-2 border">{tx.Type}</td>
            <td className="p-2 border">{tx.CreatedAt}</td>
          </tr>
        ))}
      </tbody>
    </table>
  );
}
