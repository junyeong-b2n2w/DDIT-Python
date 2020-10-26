package Day03;

import java.awt.BorderLayout;
import java.awt.EventQueue;

import javax.swing.JFrame;
import javax.swing.JPanel;
import javax.swing.border.EmptyBorder;
import javax.swing.JTextField;
import javax.swing.JLabel;
import javax.swing.JButton;
import java.awt.event.ActionListener;
import java.awt.event.ActionEvent;
import java.awt.event.MouseAdapter;
import java.awt.event.MouseEvent;

public class MyFrame04 extends JFrame {

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
					MyFrame04 frame = new MyFrame04();
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
	public MyFrame04() {
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		setBounds(100, 100, 450, 300);
		contentPane = new JPanel();
		contentPane.setBorder(new EmptyBorder(5, 5, 5, 5));
		setContentPane(contentPane);
		contentPane.setLayout(null);
		
		tf1 = new JTextField();
		tf1.setText("1");
		tf1.setBounds(12, 33, 69, 21);
		contentPane.add(tf1);
		tf1.setColumns(10);
		
		tf2 = new JTextField();
		tf2.setText("3");
		tf2.setBounds(123, 33, 69, 21);
		contentPane.add(tf2);
		tf2.setColumns(10);
		
		JLabel label = new JLabel("~");
		label.setBounds(93, 36, 19, 15);
		contentPane.add(label);
		
		JLabel label_1 = new JLabel("까지합은");
		label_1.setBounds(204, 36, 57, 15);
		contentPane.add(label_1);
		
		tf3 = new JTextField();
		tf3.setBounds(12, 74, 116, 21);
		contentPane.add(tf3);
		tf3.setColumns(10);
		
		JButton btn = new JButton("실행");
		btn.addMouseListener(new MouseAdapter() {
			@Override
			public void mouseClicked(MouseEvent e) {
				int start = Integer.parseInt(tf1.getText());
				int end = Integer.parseInt(tf2.getText());
				int total = 0;
				for(int i = start; i<=end; i++ ) {
					total = total + i;
				}
				tf3.setText(""+total);
			}
		});
	
		btn.setBounds(273, 32, 97, 23);
		contentPane.add(btn);
		
		
	}

}
