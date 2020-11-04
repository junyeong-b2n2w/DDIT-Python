package Day09;

import java.awt.BorderLayout;
import java.awt.EventQueue;

import javax.swing.JFrame;
import javax.swing.JPanel;
import javax.swing.border.EmptyBorder;
import javax.swing.JLabel;
import javax.swing.JButton;
import java.awt.event.MouseAdapter;
import java.awt.event.MouseEvent;

public class MyframeThread extends JFrame {

	private JPanel contentPane;

	/**
	 * Launch the application.
	 */
	public static void main(String[] args) {
		EventQueue.invokeLater(new Runnable() {
			public void run() {
				try {
					MyframeThread frame = new MyframeThread();
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
	public MyframeThread() {
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		setBounds(100, 100, 450, 300);
		contentPane = new JPanel();
		contentPane.setBorder(new EmptyBorder(5, 5, 5, 5));
		setContentPane(contentPane);
		contentPane.setLayout(null);
		
		JLabel lbl = new JLabel("1");
		lbl.setBounds(43, 80, 57, 15);
		contentPane.add(lbl);
		
		JButton btn = new JButton("New button");
		btn.addMouseListener(new MouseAdapter() {
			public void mouseClicked(MouseEvent e) {
				for(int i = 0; i< 1000;i++) {
					
					try {
						Thread.sleep(1000);
					} catch (Exception e2) {
					}
					lbl.setText(""+ (i+1));
					
				}
			}
		});
		btn.setBounds(138, 76, 97, 23);
		contentPane.add(btn);
	}
}
