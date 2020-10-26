package Day03;

import java.awt.BorderLayout;
import java.awt.EventQueue;

import javax.swing.JFrame;
import javax.swing.JPanel;
import javax.swing.border.EmptyBorder;
import javax.swing.JTextField;
import javax.swing.JLabel;
import javax.swing.JButton;
import java.awt.event.MouseAdapter;
import java.awt.event.MouseEvent;

public class MyFrame03 extends JFrame {

	private JPanel contentPane;
	private JTextField tf1;
	private JTextField tf2;
	private JTextField tf3;

	/**
	 * Launch the application.
	 */
	public static void main(String[] args) {
		EventQueue.invokeLater(new Runnable() {
			public void run() {
				try {
					MyFrame03 frame = new MyFrame03();
					frame.setVisible(true);
				} catch (Exception e) {
					e.printStackTrace();
				}
			}
		});
	}

	/**
	 * Create the frame.
	 */
	public MyFrame03() {
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		setBounds(100, 100, 450, 300);
		contentPane = new JPanel();
		contentPane.setBorder(new EmptyBorder(5, 5, 5, 5));
		setContentPane(contentPane);
		contentPane.setLayout(null);
		
		tf1 = new JTextField();
		tf1.setText("1");
		tf1.setBounds(12, 40, 39, 21);
		contentPane.add(tf1);
		tf1.setColumns(10);
		
		JLabel lblNewLabel = new JLabel("+");
		lblNewLabel.setBounds(63, 43, 17, 15);
		contentPane.add(lblNewLabel);
		
		tf2 = new JTextField();
		tf2.setText("2");
		tf2.setBounds(81, 40, 44, 21);
		contentPane.add(tf2);
		tf2.setColumns(10);
		
		tf3 = new JTextField();
		tf3.setBounds(205, 40, 93, 21);
		contentPane.add(tf3);
		tf3.setColumns(10);
		
		JButton btn = new JButton("=");
		btn.addMouseListener(new MouseAdapter() {
			@Override
			public void mouseClicked(MouseEvent e) {
				int num1 = Integer.parseInt(tf1.getText());
				int num2 = Integer.parseInt(tf2.getText());
				
				int result = num1 + num2;
				
				tf3.setText(""+result);
				
			}
		});
		btn.setBounds(137, 39, 44, 23);
		contentPane.add(btn);
		
		
	}

}
