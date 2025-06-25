from components.performance import compare_with_index
import plotly.graph_objects as go

perf_df = compare_with_index("AAPL", "^GSPC", start_date, end_date)
if not perf_df.empty:
    fig = go.Figure()
    for col in perf_df.columns:
        fig.add_trace(go.Scatter(x=perf_df.index, y=perf_df[col], mode='lines', name=col))
    st.plotly_chart(fig, use_container_width=True)

